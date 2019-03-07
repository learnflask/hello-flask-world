import click


@click.command()
def main():
    click.echo(f"Hello from {__name__}")
    from helloflask.app import create_app
    app = create_app()
    return app.run(debug=True)
