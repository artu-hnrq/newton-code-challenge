from .protobuf import server, rpc_api
from . import model
from . import sgbd
import logging
import click

logging.basicConfig(level=logging.INFO, format='%(message)s')
DEFAULT_PORT = 5000

@click.group()
@click.pass_context
def main(self):
    pass


@main.command()
@click.option('-p', '--port', default=DEFAULT_PORT)
def start_server(port):
    sgbd.create_table(port)
    server.start(port)


@main.command()
@click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
@click.argument('args', nargs=2, type=click.INT)
@click.option('-p', '--port', default=DEFAULT_PORT)
def request_calculation(operation, args, port):
    response = rpc_api.request_calculation(operation, args, port)
    logging.info(response)


@main.command()
@click.option('-n', '--name')
@click.option('-p', '--port', default=DEFAULT_PORT)
def connect_client(name, port):
    task = rpc_api.get_task(name, port)
    if task.work:
        model.execute(task)
    else:
        logging.info("There's no task to be done, go get some rest!")


@main.command()
@click.argument('port', default=DEFAULT_PORT)
def present_db(port):
    try:
        query = sgbd.select(port)

        logging.info('\t'.join(['ID \t\t\t\t', 'FUNC', 'RESULT']))
        for row in query:
            logging.info('\t'.join(row))
    except ValueError as e:
        logging.critical(e)

cli = click.CommandCollection(sources=[main])

if __name__ == '__main__':
    main()
