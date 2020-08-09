from .protobuf import start_server as ss, request_calculation as rc, connect_client as cc
import click


@click.group()
@click.pass_context
def main(self):
    pass


@main.command()
@click.option('-p', '--port', default=5000)
def start_server(port):
    ss(port)


@main.command()
@click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
@click.argument('numbers', nargs=2, type=click.INT)
@click.option('-p', '--port', default=5000)
def request_calculation(operation, numbers, port):
    rc(operation, numbers, port)


@main.command()
@click.option('-n', '--name')
@click.option('-p', '--port', default=5000)
def connect_client(name, port):
    cc(name, port)


#
# @main.command()
# @click.pass_context
# def s(ctx):
#     ctx.forward(start_server)
#
# @main.command()
# @click.argument('operation', type=click.Choice(['add', 'sub', 'mul', 'div']))
# @click.argument('numbers', nargs=2, type=click.INT)
# @click.pass_context
# def r(ctx):
#     ctx.forward(request_calculation)
#
# @main.command()
# @click.pass_context
# def k(ctx):
#     ctx.forward(connect_client)


cli = click.CommandCollection(sources=[main])

if __name__ == '__main__':
    main()
