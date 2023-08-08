
from todo import __app_name__, __version__
import typer

from typing import Optional

from typing_extensions import Annotated

from rich import print
from typer import Context
# pip install typer-shell
from typer_shell import make_typer_shell

# app = make_typer_shell()

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

@app.command(name="add", short_help="Adds an item")
@inner_app.command()
def create(task: str) -> None:
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
