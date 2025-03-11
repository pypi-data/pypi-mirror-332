from invoke.tasks import task


@task
def run(context, command, env):
    context.run(
        command=f"python {command}",
        env=env,
    )
