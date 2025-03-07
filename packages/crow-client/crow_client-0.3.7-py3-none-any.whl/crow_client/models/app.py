import os
import re
from enum import StrEnum, auto
from pathlib import Path
from typing import Any, ClassVar, Self, cast

from aviary.functional import EnvironmentBuilder
from ldp.agent import Agent
from ldp.alg.callbacks import Callback
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    SecretStr,
    field_serializer,
    field_validator,
    model_validator,
)

MAX_CROW_JOB_RUN_TIMEOUT = 60 * 60 * 24  # 24 hours in sec
MIN_CROW_JOB_RUN_TIMEOUT = 0  # sec


class PythonVersion(StrEnum):
    V3_11 = "3.11"
    V3_12 = "3.12"


class AuthType(StrEnum):
    GOOGLE = "google"
    PASSWORD = "password"
    API_KEY = "api_key"


class Providers(StrEnum):
    GOOGLE = "google.com"


class ProviderResponse(BaseModel):
    provider: Providers
    code: str = Field(
        description="The provider authorization code on behalf of a user. This code is emphemeral and can be used a single time in exchange for a token."
    )
    redirect_uri: str


class APIKeyPayload(BaseModel):
    api_key: str = Field(description="A user API key to authenticate with the server.")


class FirebaseCreds(BaseModel):
    email: EmailStr
    password: SecretStr

    @field_serializer("password")
    def serialize_password(self, password: SecretStr):
        return password.get_secret_value()


class PriorityQueueTypes(StrEnum):
    LOW = auto()
    NORMAL = auto()
    HIGH = auto()
    ULTRA = auto()

    def rate_percentage(self) -> float:
        if self == self.LOW:
            return 0.1
        if self == self.NORMAL:
            return 0.5
        if self == self.HIGH:
            return 0.75
        if self == self.ULTRA:
            return 1.0
        raise NotImplementedError(f"Unknown priority queue type: {self}")


class RetryConfig(BaseModel):
    """Configuration for task retry settings."""

    max_attempts: int = Field(
        -1, description="Maximum number of retry attempts. -1 for infinite retries."
    )
    max_retry_duration_seconds: int = Field(
        604800,  # 7 days in seconds
        description="Maximum time a task can be retrying for before giving up (in seconds).",
    )
    max_backoff_seconds: int = Field(
        60,  # means the rate in a full-queue will be each entry trying once per minute
        description="Maximum time to wait between retries (in seconds).",
    )
    min_backoff_seconds: int = Field(
        1, description="Minimum time to wait between retries (in seconds)."
    )
    max_doublings: int = Field(
        7,
        description="Maximum number of times the retry interval can double before becoming constant.",
    )

    def to_client_dict(self) -> dict[str, Any]:
        """Convert retry config to GCP Cloud Tasks client format."""
        return {
            "max_attempts": self.max_attempts,
            "max_retry_duration": {"seconds": self.max_retry_duration_seconds},
            "max_backoff": {"seconds": self.max_backoff_seconds},
            "min_backoff": {"seconds": self.min_backoff_seconds},
            "max_doublings": self.max_doublings,
        }


class RateLimits(BaseModel):
    """Configuration for queue rate limits."""

    max_dispatches_per_second: float = Field(
        10.0,
        description=(
            "Maximum number of tasks that can be dispatched per second."
            "If this is too high, you can overshoot the rate limit as the "
            "query to running jobs is not perfectly synchronized."
        ),
    )
    max_concurrent_dispatches: int = Field(
        100,
        description=(
            "Maximum number of concurrent tasks that can be dispatched."
            " This represents how many jobs are actively trying to get "
            "a spot as a running job at the same time. The rest will "
            "simply be waiting in the queue. The higher this is, the "
            " higher gatekeeping server load will be."
        ),
    )

    MAX_RATIO_FROM_QUEUE_SIZE: ClassVar[float] = 0.1

    @classmethod
    def from_max_queue_size(cls, max_queue_size: int) -> "RateLimits":
        """Create rate limits from a max_queue_size to avoid overwhelming the gatekeeping server."""
        return cls(
            max_concurrent_dispatches=int(
                max_queue_size * cls.MAX_RATIO_FROM_QUEUE_SIZE
            )
        )

    def to_client_dict(self) -> dict[str, Any]:
        """Convert rate limits to GCP Cloud Tasks client format."""
        return {
            "max_dispatches_per_second": self.max_dispatches_per_second,
            "max_concurrent_dispatches": self.max_concurrent_dispatches,
        }


class TaskQueue(BaseModel):
    """Configuration for a single Task Queue."""

    name: str = Field(..., description="Name of the queue")
    retry_config: RetryConfig = Field(
        default_factory=RetryConfig, description="Configuration for task retries"
    )
    rate_limits: RateLimits | None = Field(
        default=None, description="Optional rate limiting configuration"
    )
    priority_max_running_fraction: float = Field(
        default_factory=PriorityQueueTypes.NORMAL.rate_percentage,
        description=(
            "Maximum fraction of the total limit that this queue can use, proxy for priority."
            "Higher limits will essentially be preferred because they can run when "
            "lower priority queues cannot."
        ),
        ge=0.0,
        le=1.0,
    )

    @classmethod
    def from_priority_queue_type_and_max_running_jobs(
        cls, name: str, queue_type: PriorityQueueTypes, max_running_jobs: int
    ) -> "TaskQueue":
        """Create a TaskQueue from a PriorityQueueType."""
        return cls(
            name=f"{name}-{queue_type.value}",
            priority_max_running_fraction=queue_type.rate_percentage(),
            rate_limits=RateLimits.from_max_queue_size(
                int(queue_type.rate_percentage() * max_running_jobs)
            ),
        )

    def to_client_dict(self, project_id: str, location: str) -> dict[str, Any]:
        """Convert the queue configuration to GCP Cloud Tasks client format."""
        parent = f"projects/{project_id}/locations/{location}"
        queue_path = f"{parent}/queues/{self.name}"

        result = {
            "name": queue_path,
            "retry_config": self.retry_config.to_client_dict(),
        }

        if self.rate_limits:
            result["rate_limits"] = self.rate_limits.to_client_dict()

        return result


class TaskQueuesConfig(BaseModel):
    """Configuration for multiple Task Queues."""

    name: str = Field(..., description="Base name for the queue(s).")
    max_running_jobs: int = Field(
        default=30,  # low default for now
        description=(
            "Maximum concurrency for this crow job, across all queues."
            " Note: Global max across all crow jobs is 1,000, the backend will always enforce"
            " the global limit first. This limit should be set keeping in mind any dependent limits"
            " like LLM throughput."
        ),
    )
    queues: list[TaskQueue] | None = Field(
        default=None,
        description="List of task queues to be created/managed, will be built automatically if None.",
    )

    @model_validator(mode="after")
    def add_priority_queues(self):
        if self.queues is None:
            self.queues = [
                TaskQueue.from_priority_queue_type_and_max_running_jobs(
                    name=self.name,
                    queue_type=queue_type,
                    max_running_jobs=self.max_running_jobs,
                )
                for queue_type in PriorityQueueTypes
            ]
        return self

    def get_queue(self, priority_type: PriorityQueueTypes) -> TaskQueue | None:
        """Get a queue by its priority type."""
        if not self.queues:
            return None

        for queue in self.queues:
            if queue.name.endswith(f"-{priority_type.value}"):
                return queue

        return None


class Stage(StrEnum):
    DEV = "https://dev.api.platform.futurehouse.org"
    PROD = "https://api.platform.futurehouse.org"
    LOCAL = "http://localhost:8080"
    LOCAL_DOCKER = "http://host.docker.internal:8080"

    @classmethod
    def from_string(cls, stage: str) -> "Stage":
        """Convert a case-insensitive string to Stage enum."""
        try:
            return cls[stage.upper()]
        except KeyError as e:
            raise ValueError(
                f"Invalid stage: {stage}. Must be one of: {', '.join(cls.__members__)}",
            ) from e


class Step(StrEnum):
    BEFORE_TRANSITION = Callback.before_transition.__name__
    AFTER_AGENT_INIT_STATE = Callback.after_agent_init_state.__name__
    AFTER_AGENT_GET_ASV = Callback.after_agent_get_asv.__name__
    AFTER_ENV_RESET = Callback.after_env_reset.__name__
    AFTER_ENV_STEP = Callback.after_env_step.__name__
    AFTER_TRANSITION = Callback.after_transition.__name__


class FramePathContentType(StrEnum):
    TEXT = auto()
    IMAGE = auto()
    MARKDOWN = auto()
    JSON = auto()
    PDF_LINK = auto()
    PDB = auto()
    NOTEBOOK = auto()
    PQA = auto()


class FramePath(BaseModel):
    path: str = Field(
        description="List of JSON path strings (e.g. 'input.data.frame') indicating where to find important frame data. None implies all data is important and the UI will render the full environment frame as is.",
    )
    type: FramePathContentType = Field(
        default=FramePathContentType.JSON,
        description="Content type of the data at this path",
    )
    is_iterable: bool = Field(
        default=False,
        description="Content of the JSON path will be iterable, this key tell us if the rendering component should create multiple components for a single key",
    )


class DockerContainerConfiguration(BaseModel):
    cpu: str = Field(description="CPU allotment for the container")
    memory: str = Field(description="Memory allotment for the container")

    MINIMUM_MEMORY: ClassVar[int] = 2
    MAXIMUM_MEMORY: ClassVar[int] = 32

    @field_validator("cpu")
    @classmethod
    # The python library only supports 1, 2, 4, 8 CPUs
    # https://cloud.google.com/run/docs/reference/rpc/google.cloud.run.v2#resourcerequirements
    def validate_cpu(cls, v: str) -> str:
        valid_cpus = {"1", "2", "4", "8"}
        if v not in valid_cpus:
            raise ValueError("CPU must be one of: 1, 2, 4, or 8")
        return v

    @field_validator("memory")
    @classmethod
    def validate_memory(cls, v: str) -> str:
        # https://regex101.com/r/4kWjKw/1
        match = re.match(r"^(\d+)Gi$", v)

        if not match:
            raise ValueError("Memory must be in Gi format (e.g., '2Gi')")

        value = int(match.group(1))

        # GCP Cloud Run has min 512Mi and max 32Gi (32768Mi)
        # https://cloud.google.com/run/docs/configuring/services/memory-limits
        # due to the above mentioned restriction in the python client, we must
        # stay between 2Gi and 32Gi
        if value < cls.MINIMUM_MEMORY:
            raise ValueError("Memory must be at least 2Gi")
        if value > cls.MAXIMUM_MEMORY:
            raise ValueError("Memory must not exceed 32Gi")

        return v

    @model_validator(mode="after")
    def validate_cpu_memory_ratio(self) -> Self:
        cpu = int(self.cpu)

        match = re.match(r"^(\d+)Gi$", self.memory)
        if match is None:
            raise ValueError("Memory must be in Gi format (e.g., '2Gi')")

        memory_gi = int(match.group(1))
        memory_mb = memory_gi * 1024

        min_cpu_requirements = {
            2048: 1,  # 2Gi requires 1 CPU
            4096: 2,  # 4Gi requires 2 CPU
            8192: 4,  # 8Gi requires 4 CPU
            24576: 8,  # 24Gi requires 8 CPU
        }

        for mem_threshold, cpu_required in min_cpu_requirements.items():
            if memory_mb <= mem_threshold:
                if cpu < cpu_required:
                    raise ValueError(
                        f"For {self.memory} of memory, minimum required CPU is {cpu_required} CPU. Got {cpu} CPU",
                    )
                break

        return self


class CrowDeploymentConfig(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        arbitrary_types_allowed=True,  # Allows for agent: Agent | str
    )

    requirements_path: str | os.PathLike | None = Field(
        default=None,
        description="The complete path including filename to the requirements.txt file or pyproject.toml file. If not provided explicitly, it will be inferred from the path parameter.",
    )

    path: str | os.PathLike | None = Field(
        default=None,
        description="The path to your python module. Can be either a string path or Path object. "
        "This path should be the root directory of your module. "
        "This path either must include a pyproject.toml with UV tooling, or a requirements.txt for dependency resolution. "
        "Can be None if we are deploying a functional environment (through the functional_environment parameter).",
    )

    name: str | None = Field(
        default=None,
        description="The name of the crow job. If None, the crow job will be "
        "named using the included python module or functional environment name.",
    )

    environment: str = Field(
        description="Your environment path, should be a module reference if we pass an environment. "
        "Can be an arbitrary name if we are deploying a functional environment (through the functional_environment parameter). "
        "example: dummy_env.env.DummyEnv",
    )

    functional_environment: EnvironmentBuilder | None = Field(
        default=None,
        description="An object of type EnvironmentBuilder used to construct an environment. "
        "Can be None if we are deploying a non functional environment.",
    )

    requirements: list[str] | None = Field(
        default=None,
        description="A list of dependencies required for the deployment, similar to the Python requirements.txt file. "
        "Each entry in the list specifies a package or module in the format used by pip (e.g., 'package-name==1.0.0'). "
        "Can be None if we are deploying a non functional environment (functional_environment parameter is None)",
    )

    environment_variables: dict[str, str] | None = Field(
        default=None,
        description="Any key value pair of environment variables your environment needs to function.",
    )

    container_config: DockerContainerConfiguration | None = Field(
        default=None,
        description="The configuration for the cloud run container.",
    )

    python_version: PythonVersion = Field(
        default=PythonVersion.V3_12,
        description="The python version your docker image should build with.",
    )

    agent: Agent | str = Field(
        default="ldp.agent.SimpleAgent",
        description="Your desired agent path, should be a module reference and a fully qualified name. "
        "example: ldp.agent.SimpleAgent",
    )

    requires_aviary_internal: bool = Field(
        default=False,
        description="Indicates your project requires aviary-internal to function. "
        "This is only necessary for envs within aviary-internal.",
    )

    timeout: int | None = Field(
        default=600,
        description="The amount of time in seconds your crow will run on a task before it terminates.",
        ge=MIN_CROW_JOB_RUN_TIMEOUT,
        le=MAX_CROW_JOB_RUN_TIMEOUT,
    )

    force: bool = Field(
        default=False,
        description="If true, immediately overwrite any existing job with the same name.",
    )

    storage_location: str = Field(
        default="storage",
        description="The location the container will use to mount a locally accessible GCS folder as a volume. "
        "This location can be used to store and fetch files safely without GCS apis or direct access.",
    )

    frame_paths: list[FramePath] | None = Field(
        default=None,
        description="List of FramePath which indicates where to find important frame data, and how to render it.",
    )

    markdown_template_path: str | os.PathLike | None = Field(
        default=None,
        description="The path to the markdown template file. This file will be dynamically built within the environment frame section of the UI. "
        "The keys used in the markdown file follow the same requirement as FramePath.path. None implies no markdown template is present and the UI "
        "will render the environment frame as is.",
    )

    task_queues_config: TaskQueuesConfig | None = Field(
        default=None,
        description="The configuration for the task queue(s) that will be created for this deployment.",
    )

    @field_validator("markdown_template_path")
    @classmethod
    def validate_markdown_path(
        cls, v: str | os.PathLike | None
    ) -> str | os.PathLike | None:
        if v is not None:
            path = Path(v)
            if path.suffix.lower() not in {".md", ".markdown"}:
                raise ValueError(
                    f"Markdown template must be a .md or .markdown extension: {path}"
                )
        return v

    task_description: str | None = Field(
        default=None,
        description="Override for the task description, if not included it will be pulled from your "
        "environment `from_task` docstring. Necessary if you are deploying using an Environment class"
        " as a dependency.",
    )

    @field_validator("path")
    @classmethod
    def validate_module_path(cls, value: str | os.PathLike) -> str | os.PathLike:
        path = Path(value)
        if not path.exists():
            raise ValueError(f"Module path {path} does not exist")
        if not path.is_dir():
            raise ValueError(f"Module path {path} is not a directory")
        return value

    @field_validator("requirements_path")
    @classmethod
    def validate_requirements_path(
        cls, value: str | os.PathLike | None
    ) -> str | os.PathLike | None:
        if value is None:
            return value

        path = Path(value)
        if not path.exists():
            raise ValueError(f"Requirements path {path} does not exist")
        if not path.is_file():
            raise ValueError(f"Requirements path {path} is not a file")
        if path.suffix not in {".txt", ".toml"}:
            raise ValueError(f"Requirements path {path} must be a .txt or .toml file")
        return value

    @model_validator(mode="after")
    def validate_path_and_requirements(self) -> Self:
        if self.path is None:
            return self

        path = Path(self.path)
        requirements_path = (
            Path(self.requirements_path) if self.requirements_path else None
        )

        if not (
            (path / "pyproject.toml").exists()
            or (path / "requirements.txt").exists()
            or (requirements_path and requirements_path.exists())
        ):
            raise ValueError(
                f"Module path {path} must contain either pyproject.toml or requirements.txt, "
                f"or a valid requirements_path must be provided"
            )

        if not self.task_queues_config:
            self.task_queues_config = TaskQueuesConfig(name=self.job_name)

        return self

    @field_validator("environment")
    @classmethod
    def validate_environment_path(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Environment path cannot be empty")
        if not all(part.isidentifier() for part in value.split(".")):
            raise ValueError(f"Invalid environment path format: {value}")
        return value

    @field_validator("agent")
    @classmethod
    def validate_agent_path(cls, value: Agent | str) -> Agent | str:
        if isinstance(value, Agent):
            return value

        if not value or not value.strip():
            raise ValueError("Agent path cannot be empty")
        if not all(part.isidentifier() for part in value.split(".")):
            raise ValueError(f"Invalid agent path format: {value}")
        return value

    @property
    def module_name(self) -> str:
        if not self.path and not self.functional_environment:
            raise ValueError(
                "No module specified, either a path or a functional environment must be provided."
            )
        return (
            Path(self.path).name
            if self.path
            else cast(EnvironmentBuilder, self.functional_environment).__name__  # type: ignore[attr-defined]
        )

    @property
    def job_name(self) -> str:
        """Name to be used for the crow job deployment."""
        return self.name or self.module_name
