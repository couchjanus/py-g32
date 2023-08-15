
from todo import __app_name__, __version__, ERRORS, database, controller
import typer

from typing import Optional

from typing_extensions import Annotated

from rich import print
from typer import Context
# pip install typer-shell
from typer_shell import make_typer_shell
from pathlib import Path
# app = make_typer_shell()

from typing import List

app = make_typer_shell(prompt="🔥: ", params={"name": "Bob"}, params_path="params.yaml")
inner_app = make_typer_shell(prompt="🌲: ", params={"name": "Bob"}, params_path="innerparams.yaml")
app.add_typer(inner_app, name="dialog", help="Run program in dialogue mode")


# dialog_app = make_typer_shell(prompt="😎: ")

# app.add_typer(dialog_app, name="dialog", help="Run program in dialogue mode")

# app = typer.Typer()
state = {"verbose": False}

@app.command()
def about():
    typer.echo(
   f"""
   💬 {__app_name__.title()} is a command-line interface application
   built with Typer(https://typer.tiangolo.com/)
   to help You manage your to-do list.
   You can also access the help message for specific commands by typing
   the command and then `--help`. For example, to display the help content
   for the `add` command, you can run the following:
   python -m {__app_name__} add --help
   """
    )

# init database
@app.command()
def init(db_path: str = typer.Option(str(database.DEFAULT_DB_FILE_PATH), "--db-path", "-d", prompt="TODO database location? ")) -> None:
    """Initialize the TODO database."""
    app_init_error = database.init_app(db_path)
    if app_init_error:
        typer.secho(
          f"Creating config file failed with {ERRORS[app_init_error]}",
          fg="red"   
        )
        raise typer.Exit(1)
    
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
          f"Creating database file failed with {ERRORS[db_init_error]}", 
          fg="red"  
        )
        raise typer.Exit(1)
    
    else:
        typer.secho(
            f"The {__app_name__} database is {db_path}",
            fg="green"
        )


def get_todo()->controller.Todo:
    if database.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(database.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "todo init"', 
            fg="red"
            
        )
        raise typer.Exit(1)
    if db_path.exists():
        return controller.Todo(db_path)
    else:
        typer.secho(
            'Database not found. Please< run "todo init"',
            fg="red"
        )
        raise typer.Exit(1)

@app.command(name="add", short_help="Adds an item")
@inner_app.command()
def add(
    task: List[str] = typer.Argument(...),
    priority: int = typer.Option(2, "--priority", "-p", min=1, max=3),
    ) -> None:
    """Add a new task with description to todo list."""
    todos = get_todo()
    todo, error = todos.add(task, priority)
    if error:
        typer.secho(
            f'Added todo failed with "{ERRORS[error]}"', fg="red"
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"""todo: "{task}" was added """
            f"""with priority: {priority}""",
            fg="green"
        )
    if state["verbose"]:
        print(f"💬 Just added a {task}")

@app.command(name="remove", short_help="Remove an item")
@inner_app.command()
def delete(id: int) -> None:
    print(f"Hello {id}")

@app.command(name="update", short_help="Update an item")
def edit(id: int) -> None:
    print(f"Hello {id}")
    
def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"💬 {__app_name__} version: {__version__}")
        raise typer.Exit()

@app.callback()
def main(
        verbose: bool = False,
        version: Annotated[
            Optional[bool],
            typer.Option(
                "--version", 
                "-v",
                help="Show the application's version and exit.",
                callback=_version_callback,
                is_eager=True
            )
        ] = None 
        ) -> None:
    """
    Manage todos in the CLI application
    
    _summary_

    Args:
        verbose (bool, optional): _description_. Defaults to False.
    """
    if verbose:
        state["verbose"] = True
    return
