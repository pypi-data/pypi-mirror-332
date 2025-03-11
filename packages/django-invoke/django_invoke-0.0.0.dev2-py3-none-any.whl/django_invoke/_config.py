import dataclasses
import collections

import invoke


@dataclasses.dataclass
class DockerSettings:
    main_containers: collections.abc.Sequence[str] = (
        "postgres",
        "redis",
    )
    compose_cmd = "docker-compose"


@dataclasses.dataclass
class DjangoSettings:
    """Settings for django module."""

    runserver_command: str = "runserver_plus"
    runserver_host: str = "0.0.0.0"  # noqa: S104
    runserver_port: str = "8000"
    runserver_params: str = ""
    runserver_docker_params: str = "--rm --service-ports"
    migrate_command: str = "migrate"
    makemessages_params: str = "--all --ignore venv"
    verbose_email_name: str = "Email address"
    default_superuser_email: str = "root@localhost"
    verbose_username_name: str = "Username"
    default_superuser_username: str = "root"
    verbose_password_name: str = "Password"
    default_superuser_password: str = "root"
    shell_command: str = "shell_plus --ipython"
    path_to_remote_config_file: str = "/workspace/app/config/settings/.env"
    manage_file_path: str = "./manage.py"
    settings_path: str = "settings.local"


@dataclasses.dataclass(frozen=True)
class Config:
    project_name: str = ""

    docker: DockerSettings = dataclasses.field(
        default_factory=DockerSettings,
    )
    django: DjangoSettings = dataclasses.field(
        default_factory=DjangoSettings,
    )

    @classmethod
    def from_context(cls, context: invoke.Context) -> "Config":
        """Get config from invoke context."""
        return context.config.get(
            "django_invoke",
            cls(),
        )
