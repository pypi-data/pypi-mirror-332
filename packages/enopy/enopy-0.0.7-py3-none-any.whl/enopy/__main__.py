import click
import uvicorn

from fans.path import Path

from enopy.parse import parse_eno


@click.group()
def cli():
    pass


@cli.command()
@click.option('-p', '--port', default = 9999, help = 'Port to listening on')
@click.option('-r', '--reload', is_flag = True)
def serve(port, reload):
    """
    Run server
    """
    uvicorn.run('eno.server.app:app', host = '127.0.0.1', port = port, reload = reload)


@cli.command()
@click.argument('path')
def parse(path):
    """
    Parse text
    """
    with Path(path).open() as f:
        text = f.read()
    res = parse_eno(text)
    print(res)


if __name__ == '__main__':
    cli()
