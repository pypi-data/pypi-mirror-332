"""The Flexdown CLI.""" ""

from pathlib import Path

import typer
from reflex.utils.processes import new_process
from reflex.constants import Env, LogLevel

from flexdown import constants

# The command line app.
app = typer.Typer()


@app.command()
def run(
    path: Path,
    deploy: bool = typer.Option(False, help="Deploy the project after running."),
    deploy_project: str = typer.Option(None, help="The project to deploy."),
    token: str = typer.Option(
        None, "-t", "--token", help="The token to use for deployment."
    ),
    env: Env | None = typer.Option(None, help="The environment to run the project in."),
    enterprise: bool = typer.Option(
        False,
        "-e",
        "--enterprise",
        help="Whether to use the enterprise app template.",
    ),
    loglevel: LogLevel | None = typer.Option(None, help="The log level to use."),
):
    """Run a Flexdown project."""
    # Create a .flexdown directory in the current directory.
    constants.FLEXDOWN_DIR.mkdir(parents=True, exist_ok=True)

    # Create a reflex project.
    if not (constants.FLEXDOWN_DIR).exists():
        command = ["reflex", "init", "--template", "blank"]

        if loglevel is not None:
            command.extend(["--loglevel", loglevel])

        new_process(command, cwd=constants.FLEXDOWN_DIR, show_logs=True, run=True)

    # Replace the app file with a template.
    write_app_content(path, enterprise)

    command = ["reflex"]
    if deploy:
        if not token:
            return typer.echo("A token is required for deployment.")
        if not deploy_project:
            return typer.echo("A project is required for deployment.")
        if env:
            return typer.echo("The environment flag cannot be used with deployment.")
        command.extend(["deploy", "--token", token, "--project", deploy_project])
    else:
        command.extend("run")

    if loglevel is not None:
        command.extend(["--loglevel", loglevel])

    match env:
        case Env.DEV:
            command.extend(["--env", "dev"])
        case Env.PROD:
            command.extend(["--env", "prod"])

    # Run the reflex project.
    new_process(command, cwd=constants.FLEXDOWN_DIR, show_logs=True, run=True)


def write_app_content(path: Path, enterprise: bool) -> None:
    """Write the content for the app file.

    Args:
        path: The path to the Flexdown project.
        enterprise: Whether to use the enterprise app template.
    """
    constants.FLEXDOWN_FILE.write_text(get_app_content(path, enterprise))


def get_app_content(path: Path, enterprise: bool) -> str:
    """Format the content of the root app file for flexdown.

    Args:
        path: The path to the Flexdown project.
        enterprise: Whether to use the enterprise app template.

    Returns:
        The content for the app file.
    """
    return constants.APP_TEMPLATE.format(
        path=Path().absolute() / path,
        module_name=path.stem,
        app_init=constants.ENTERPRISE_APP_INIT
        if enterprise
        else constants.DEFAULT_APP_INIT,
    )
