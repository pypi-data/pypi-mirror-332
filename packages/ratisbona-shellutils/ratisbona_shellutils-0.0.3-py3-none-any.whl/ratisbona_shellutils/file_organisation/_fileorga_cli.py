import re
import sys
from pathlib import Path

import click

from ratisbona_shellutils.cli import blue_dosbox
from ratisbona_utils.io import errprint
from ratisbona_utils.strings import cleaners, string_cleaner

ERR={"file": sys.stderr}

def print_mv(src: str, dst: str):
    if src == dst:
        print(f"# No change, skipping {src}", **ERR)
        return
    move_command = "mv -i -v "
    padding = " " * len(move_command)
    print(f"{move_command}\"{src}\" \\\n{padding}\"{dst}\"")



@click.group()
@click.pass_context
def fileorga_cli(ctx):
    errprint(blue_dosbox("    Ratisbona File Organisation CLI"))
    ctx.ensure_object(dict)

@fileorga_cli.command()
@click.argument("regexp", type=str)
@click.argument("replacement", type=str)
@click.argument('args', nargs=-1)
def regexp(the_regexp: str, replacement: str, args: list[str]):
    """
    Rename files using a regular expression.

    The regular expression is applied to the filename. The replacement string is used to create the new filename.

    Args:
        the_regexp (str): The regular expression to match the filename
        replacement (str): The replacement string. You can use \\1, \\2, ... to refer to the matched groups.
        args (list[str]): The files to rename
    """
    for src in args:
        full_path = Path(src)
        file_name = full_path.name
        file_path = full_path.parent
        dst = re.sub(the_regexp, replacement, file_name)
        dst_path = file_path / dst
        print_mv(src, str(dst_path))

@fileorga_cli.command()
@click.argument('args', nargs=-1)
def cut_otr_postfix(args: list[str]):
    regexp(
        the_regexp=r"_([0-9]{2}[\._-])+[a-z0-9]+_[0-9]{1,3}_TVOON_DE(\.mpg)?(\.HQ)?",
        replacement="",
        args=args
    )


@fileorga_cli.command()
@click.argument('args', nargs=-1)
@click.option('--verbose', '-v', is_flag=True, help="Show details on filename cleanup on stderr")
def rename(verbose: bool, args: list[str], **kwargs):
    apply_cleaners = []

    if kwargs.get('all'):
        apply_cleaners.extend(cleaners.keys())

    for cleaner in cleaners:
        gui_name = cleaner.replace("_", "-")
        if kwargs.get(gui_name):
            if not cleaner in apply_cleaners:
                apply_cleaners.append(cleaner)
        if kwargs.get(f'no-{gui_name}'):
            apply_cleaners.remove(cleaner)

    def change_callback(cleaner, original_string, new_string):
        newfilestart = "->"
        if verbose:
            print(f"# {cleaner:20s}: {original_string}", **ERR)
            print(f"# {newfilestart:20s}: {new_string}", **ERR)
            print(**ERR)

    for src in args:
        full_path = Path(src)
        file_name = full_path.name
        file_path = full_path.parent
        dst = string_cleaner(file_name, apply_cleaners, change_callback=change_callback)
        dst_path = file_path / dst
        print_mv(src, str(dst_path))

# Dynamically add cleaners
for option, (the_function, the_help) in cleaners.items():
    option=option.replace("_", "-")
    rename = click.option(f'--{option}', is_flag=True, help=f"Enable {option}: " + the_help)(rename)
    rename = click.option(f'--no-{option}', is_flag=True, help=f"Disable {option}: " + the_help)(rename)
rename = click.option('--all', is_flag=True, help="Enable all cleaners")(rename)
