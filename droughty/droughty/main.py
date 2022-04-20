import typer
import click

from dataclasses import dataclass


from droughty import lookml_cli 
from droughty import dbt_test_cli
from droughty import dbml_cli
from droughty import cube_cli
from droughty import config_cli

app = typer.Typer()

app.add_typer(lookml_cli.app, name="lookml")
app.add_typer(dbt_test_cli.app, name="dbt")
app.add_typer(dbml_cli.app, name="dbml")
app.add_typer(cube_cli.app, name="cube")

## app.add_typer(config_cli.app)

#####

cli_profile_path = []

@dataclass
class Common:
    profile_dir: str

@app.callback()
def common(ctx: typer.Context,
           profile_dir: str = typer.Option(..., )):

    typer.echo(f"Hello {profile_dir}")

    cli_path = """{}""".format(profile_dir)

    cli_profile_path.append(profile_dir)


    """Common Entry Point"""
    ctx.obj = Common(profile_dir)

if __name__ == "__main__":
    app()