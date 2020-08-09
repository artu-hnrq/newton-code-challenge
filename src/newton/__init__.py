from .protobuf import start_server as ss, request_calculation as rc, connect_client as cc
import click


@click.group()
@click.pass_context
def main(self):
    pass


@main.command()
def start_server():
    ss()


@main.command()
@click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
@click.argument('numbers', nargs=2, type=click.INT)
def request_calculation(operation, numbers):
    rc(operation, numbers)


@main.command()
def connect_client():
    cc()


cli = click.CommandCollection(sources=[main])

if __name__ == '__main__':
    main()
