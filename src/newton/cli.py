from .protobuf import server, rpc_api
from . import model
import logging
import click


@click.group()
@click.pass_context
def main(self):
    pass


@main.command()
@click.option('-p', '--port', default=5000)
def start_server(port):
    server.start(port)


@main.command()
@click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
@click.argument('args', nargs=2, type=click.INT)
@click.option('-p', '--port', default=5000)
def request_calculation(operation, args, port):
    response = rpc_api.request_calculation(operation, args, port)
    logging.info(response)


@main.command()
@click.option('-n', '--name')
@click.option('-p', '--port', default=5000)
def connect_client(name, port):
    calculations = rpc_api.get_task(name, port)
    model.execute(calculations)


cli = click.CommandCollection(sources=[main])

if __name__ == '__main__':
    main()
