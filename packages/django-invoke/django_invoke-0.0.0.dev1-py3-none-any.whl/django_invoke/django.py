import datetime as dt
import os

import invoke
from invoke.exceptions import Failure
from invoke.watchers import FailingResponder, Responder

from . import _config, printer, python


@invoke.task
def manage(context, command):
    """Run ``manage.py`` command.

    This command also handle starting of required services and waiting DB to
    be ready.

    Args:
        context: Invoke context
        command: Manage command
        watchers: Automated responders to command

    """
    config = _config.Config.from_context(context)
    env = {
        "DJANGO_SETTINGS_MODULE": config.django.settings_path,
    }

    return python.run(
        context,
        " ".join([
            config.django.manage_file_path,
            command
        ]),
        env=env,
    )


@invoke.task
def run(context):
    """Run development web-server."""
    config = _config.Config.from_context(context)
    printer.success("Running web app")
    manage(context, config.django.runserver_command)


@invoke.task(
    optional=['app_label', 'migration_name'],
)
def migrate(context, app_label=None, migration_name=None):
    """Apply migrations. Can be used to revert a migration."""
    config = _config.Config.from_context(context)
    printer.success("Running migrations")
    if app_label and migration_name:
        command = f"{config.django.migrate_command} {app_label} {migration_name}"
    elif app_label:
        command = f"{config.django.migrate_command} {app_label}"
    else:
        command = config.django.migrate_command
    manage(
        context,
        command,
    )


@invoke.task
def makemigrations(context):
    """Run makemigrations command and chown created migrations."""
    printer.success("Making migrations")
    manage(context, command="makemigrations")


@invoke.task
def check_new_migrations(context: invoke.Context) -> None:
    """Check if there is new migrations or not."""
    printer.success("Django: Checking migrations")
    manage(
        context,
        command="makemigrations --check --dry-run",
    )

@invoke.task
def resetdb(
    context,
    apply_migrations: bool = True,
) -> None:
    """Reset database to initial state (including test DB).

    Requires django-extensions:
        https://django-extensions.readthedocs.io/en/latest/installation_instructions.html

    """
    printing.success("Reset database to its initial state")
    manage(context, command="drop_test_database --noinput")
    manage(context, command="reset_db -c --noinput")
    if not apply_migrations:
        return
    makemigrations(context)
    migrate(context)
    createsuperuser(context)
    set_default_site(context)


@invoke.task
def shell(
    context: invoke.Context,
    params: str = "",
) -> None:
    """Shortcut for manage.py shell command.

    Requires django-extensions:
        https://django-extensions.readthedocs.io/en/latest/installation_instructions.html

    Additional params available here:
        https://django-extensions.readthedocs.io/en/latest/shell_plus.html

    """
    printer.success("Entering Django Shell")
    config = _config.Config.from_context(context)
    manage(
        context,
        command=f"{config.django.shell_command} {params}",
    )


@invoke.task
def dbshell(context: invoke.Context) -> None:
    """Open database shell with credentials from either local or dev env."""
    printer.success("Entering DB shell")
    manage(context, command="dbshell")
