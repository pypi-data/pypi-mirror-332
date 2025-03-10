import sys
from re import finditer

import click
from ratisbona_utils.io import errprint

from ratisbona_shellutils.cli import blue_dosbox
from ratisbona_utils.strings import (
    sclean_transliterate,
    sclean_unidecode,
    si_format_number,
)

ERR = {"file": sys.stderr}


@click.group()
def piper_cli():
    errprint(blue_dosbox("Ratisbona Piper CLI"))



@piper_cli.command()
def unicode_filter():
    for line in sys.stdin:
        sys.stdout.write(sclean_unidecode(line))


@piper_cli.command()
def transliterate():
    for line in sys.stdin:
        sys.stdout.write(sclean_transliterate(line))


@piper_cli.command()
@click.option("--left-align", "-l", is_flag=True, help="Align numbers to the left")
def number_format(left_align: bool = False):
    the_re = r"\d{3,}"

    for line in sys.stdin:
        matches = finditer(the_re, line)
        start = 0
        for match in matches:
            print(line[start : match.span()[0]], end="")
            print(mangle_number(match.group(0), left_align), end="")
            start = match.span()[1]
        print(line[start:], end="")


def mangle_number(the_input: str, left_align: bool) -> str:
    the_number = int(the_input)
    the_format = si_format_number(the_number)
    the_difference = max(len(the_input) - len(the_format), 0)
    padding = " " * the_difference
    return the_format + padding if left_align else padding + the_format
