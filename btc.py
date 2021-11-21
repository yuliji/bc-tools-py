from pycoin.symbols.btc import network as BTC
import click
import subprocess


@click.group()
def cli():
    pass


@cli.command()
@click.option('--address', prompt='address',
              help='The address')
@click.option('--signature', prompt='signature',
              help='The signature')
@click.option('--message', prompt='message',
              help='Message')
def verify_signature(address, signature, message):
    ok = BTC.msg.verify(address, signature, message)
    print(f'verify: {ok}')


@cli.command()
@click.option('--hex', prompt='hex',
              help='hex of txn')
def txn_from_hex(hex):
    subprocess.call(['tx', hex])


def main():
    cli()
