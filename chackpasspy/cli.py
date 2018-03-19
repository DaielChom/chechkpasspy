# -*- coding: utf-8 -*-

"""Console script for chackpasspy."""
import sys
import click
from chackpasspy.chackpasspy import checkio


@click.command()
@click.argument('passw', type=str)
def main(passw):
    """Console script for chackpasspy."""
    if(checkio(passw)):
        click.echo("Contraseña Valida")
    else:
        click.echo("Contraseña no Valida")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
