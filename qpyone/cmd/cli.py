import typer as typer


# overall cli api entry point

app = typer.Typer(name="fluent-app")


def add_typer(name: str, app: typer.Typer, **kwargs) -> typer.Typer:
    """
    add typer to base api
    :param name:
    :param app:
    :param kwargs:
    :return:
    """
    app.add_typer(app, name=name)
    return app
