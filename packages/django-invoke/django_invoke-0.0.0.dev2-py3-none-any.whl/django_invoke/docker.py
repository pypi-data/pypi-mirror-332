from invoke.exceptions import UnexpectedExit
from invoke.tasks import task
import pathlib

from . import _config, printer


@task
def up(context):
    config = _config.Config.from_context(context)
    if not any(
        pathlib.Path(compose_file).exists()
        for compose_file in (
            "compose.yaml",
            "compose.yml",
            "docker-compose.yaml",
            "docker-compose.yml",
        )
    ):
        printer.info("No docker-compose file found.")
        return
    if not config.docker.main_containers:
        printer.info("No main containers defined.")
        return
    up_containers(
        context,
        containers=config.docker.main_containers,
        detach=True,
    )

@task
def stop(context):
    """Stop main containers."""
    config = _config.Config.from_context(context)
    if not any(
        pathlib.Path(compose_file).exists()
        for compose_file in (
            "compose.yaml",
            "compose.yml",
            "docker-compose.yaml",
            "docker-compose.yml",
        )
    ):
        printer.info("No docker-compose file found.")
        return
    if not config.docker.main_containers:
        printer.info("No main containers defined.")
        return
    up_containers(
        context,
        containers=config.docker.main_containers,
        detach=True,
    )
    stop_containers(
        context,
        containers=config.docker.main_containers,
    )

def up_containers(
    context,
    containers: tuple[str],
    detach=True,
    stop_others=True,
    **kwargs,
):
    """Bring up containers and run them.

    Add `d` kwarg to run them in background.

    Args:
        context: Invoke context
        containers: Name of containers to start
        detach: To run them in background
        stop_others: Stop ALL other containers in case of errors during `up`.
            Usually this happens when containers from other project uses the
            same ports, for example, Postgres and redis.

    Raises:
        UnexpectedExit: when `up` command wasn't successful

    """
    if containers:
        printer.success(f"Bring up {', '.join(containers)} containers")
    else:
        printer.success("Bring up all containers")
    up_cmd = (
        f"docker-compose -f docker-compose.yml up --build "
        f"{'-d ' if detach else ''}"
        f"{' '.join(containers)}"
    )
    try:
        context.run(up_cmd)
    except UnexpectedExit as exception:
        if not stop_others:
            raise exception
        stop_all_containers(context)
        context.run(up_cmd)


def stop_containers(
    context,
    containers,
) -> None:
    """Stop containers."""
    printer.success(f"Stopping {' '.join(containers)} containers")
    compose_cmd = _config.Config.from_context(context).docker.compose_cmd
    context.run(f"{compose_cmd} stop {' '.join(containers)}")


def stop_all_containers(context):
    """Shortcut for stopping ALL running docker containers."""
    context.run("docker stop $(docker ps -q)")


@task
def clear(context):
    """Stop and remove all containers defined in docker-compose.

    Also remove images.

    """
    printer.success("Clearing docker-compose")
    context.run("docker-compose -f docker-compose.yml rm")
    context.run("docker-compose down -v --rmi all --remove-orphans")
