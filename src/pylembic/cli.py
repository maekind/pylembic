import typer

from pylembic.validator import Validator

app = typer.Typer(
    help="pylembic CLI for validating and visualizing Alembic migrations."
)


@app.command()
def main(
    migrations_path: str = typer.Argument(
        default="migrations", help="Path to the migrations folder."
    ),
    validate: bool = typer.Option(False, "--validate", help="Validate the migrations."),
    show_graph: bool = typer.Option(
        False, "--show-graph", help="Visualize the migration dependency graph."
    ),
    verbose: bool = typer.Option(
        False, "--verbose", help="Show migrations validation logs."
    ),
    check_branching: bool = typer.Option(
        False, "--check-branching", help="Include branching in the validation."
    ),
):
    """
    Main command to validate and/or visualize migrations.
    """
    if verbose:
        typer.echo("Verbose mode enabled.")

    if check_branching:
        typer.echo("Check for branching migrations enabled.")

    typer.echo(f"Processing migrations in: {migrations_path}")
    validator = Validator(migrations_path)

    if validate:
        typer.echo("Validating migrations...")

        if validator.validate(branching=check_branching):
            typer.secho("Migrations validation passed!", fg=typer.colors.GREEN)
        else:
            typer.secho("Migrations validation failed!", fg=typer.colors.RED)

    if show_graph:
        typer.echo("Visualizing migration graph...")
        validator.show_graph()

    if not validate and not show_graph:
        typer.echo("No action specified. Use --help for more information.")


if __name__ == "__main__":
    app()
