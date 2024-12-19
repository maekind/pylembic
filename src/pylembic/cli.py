import typer

from pylembic.validator import Validator

app = typer.Typer(
    help="pylembic CLI for validating and visualizing Alembic migrations.",
    invoke_without_command=True,
)


@app.callback()
def main(ctx: typer.Context):
    """
    Entry point for the CLI tool.
    """
    if not ctx.invoked_subcommand:
        typer.echo("No command specified. Use --help for more information.")


@app.command()
def validate(
    migrations_path: str = typer.Argument(
        default="migrations", help="Path to the migrations folder."
    ),
    verbose: bool = typer.Option(
        False, "--verbose", help="Show migrations validation logs."
    ),
    detect_branches: bool = typer.Option(
        False, "--detect-branches", help="Include branching in the validation."
    ),
):
    """
    Validate the migrations in the specified path.
    """
    if verbose:
        typer.echo("Verbose mode enabled.")

    if detect_branches:
        typer.echo("Detecting for branching migrations enabled.")

    typer.echo(f"Processing migrations in: {migrations_path}")
    validator = Validator(migrations_path)

    typer.echo("Validating migrations...")
    if validator.validate(detect_branches=detect_branches, verbose=verbose):
        typer.secho("Migrations validation passed!", fg=typer.colors.GREEN)
    else:
        typer.secho("Migrations validation failed!", fg=typer.colors.RED)


@app.command()
def show_graph(
    migrations_path: str = typer.Argument(
        default="migrations", help="Path to the migrations folder."
    ),
):
    """
    Visualize the migration dependency graph.
    """
    typer.echo(f"Processing migrations in: {migrations_path}")
    validator = Validator(migrations_path)

    typer.echo("Visualizing migration graph...")
    validator.show_graph()


if __name__ == "__main__":
    app()
