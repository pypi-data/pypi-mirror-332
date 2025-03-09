import click
from fastapi_forge.frontend import init


@click.group()
def main() -> None:
    """FastAPI Forge CLI."""


@main.command()
@click.option(
    "--use-defaults",
    is_flag=True,
    help="Use default values for project creation.",
)
@click.option(
    "--no-ui",
    is_flag=True,
    help="Create a new project without UI for testing.",
)
def start(use_defaults: bool, no_ui: bool) -> None:
    """Start the server, and open the browser."""
    init(use_defaults=use_defaults, no_ui=no_ui)


@main.command()
def dry_run() -> None:
    """Run cookiecutter without generating files."""


@main.command()
def version() -> None:
    """Print the version of FastAPI Forge."""
    from importlib.metadata import version

    click.echo(f"FastAPI Forge v{version('fastapi-forge')}.")


if __name__ in {"__main__", "__mp_main__"}:
    main()
