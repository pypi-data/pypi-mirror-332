## django-invoke
[![PyPI](https://img.shields.io/pypi/v/django-invoke.svg)](https://pypi.org/project/django-invok/)

Collection of frequently used tasks for Django development. It's built on top of [invoke](https://github.com/pyinvoke/invoke) to streamline how to manage task execution.

### Configuration
Add a `tasks.py` to your project
```
import invoke

import django_invoke

ns = invoke.Collection(
    django_invoke.docker,
    django_invoke.django,
)


# # Configurations for run command
ns.configure(
    dict(
        run=dict(
            pty=True,
            echo=True,
        ),
        django_invoke=django_invoke.Config(
            docker=django_invoke.DockerSettings(
                main_containers=["container1", "container2"],
            ),
            django=django_invoke.DjangoSettings(
                settings_path="<relative/path/to/django_settings>",
            ),
        )
    ),
)
```

### Usage
Here a few commands that you can use:
```
inv docker.up
inv docker.stop
inv django.run
inv django.migrate
inv django.makemigrations
inv django.check-new-migrations
inv django.db
inv django.dbshell
```
