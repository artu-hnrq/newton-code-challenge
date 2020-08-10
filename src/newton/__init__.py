from .protobuf import server, rpc_api
from . import model, dbms
import click, logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
DEFAULT_PORT = 5000

@click.group()
@click.pass_context
def main(self):
    pass


@main.command()
@click.option('-p', '--port', default=DEFAULT_PORT)
def start_server(port):
    try:
        dbms.create_table(port)
        server.start(port)
    except Exception as e:
        logging.critical(f"Something went wrong: {e}")


@main.command()
@click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
@click.argument('args', nargs=2, type=click.INT)
@click.option('-p', '--port', default=DEFAULT_PORT)
def request_calculation(operation, args, port):
    try:
        response = rpc_api.request_calculation(operation, args, port)
        logging.info(response)
    except:
        logging.warning(f"There's no server running at port {port}")


@main.command()
@click.option('-n', '--name')
@click.option('-p', '--port', default=DEFAULT_PORT)
def connect_client(name, port):
    try:
        task = rpc_api.get_task(name, port)

        if task.work:
            model.execute(task)
        else:
            logging.info("There's no task to be done, go get some rest!")

    except:
        logging.warning(f"There's no server running at port {port}")


@main.command()
@click.argument('port', default=DEFAULT_PORT)
def present_db(port):
    try:
        query = dbms.select(port)

        logging.info('\t'.join(['ID \t\t\t\t', 'FUNC', 'RESULT']))
        for row in query:
            logging.info('\t'.join(row))
    except:
        logging.critical(f"There's no record of a server with id {port}")


if __name__ == '__main__':
    main()
