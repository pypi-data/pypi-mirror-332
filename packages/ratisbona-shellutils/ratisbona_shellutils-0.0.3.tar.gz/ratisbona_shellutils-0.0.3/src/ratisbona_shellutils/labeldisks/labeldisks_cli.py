from pathlib import Path
from typing import Iterable

import click
import importlib.resources as pkg_resources

from ratisbona_shellutils import resources
from ratisbona_utils.functional._functional import ensure_iterator
from ratisbona_utils.io import UTF8

from ratisbona_shellutils.cli import blue_dosbox
from ratisbona_shellutils.labeldisks._labeldisks import (
    update_diskinfo_dict,
    load_stats,
    get_statfile_path,
    lsblk_diskinfo,
    print_disk_info,
    save_stats,
)


@click.group()
def label_disks_cli():
    print(blue_dosbox("Label Disks"))
    print()


@label_disks_cli.command("scan")
def scan_cli():
    stat_file = get_statfile_path()
    print("Opening stat file at", stat_file)
    saved_disk_infos = load_stats(stat_file)

    print("Updating disk infos...")
    disk_infos = lsblk_diskinfo()
    for disk_info in disk_infos:
        update_diskinfo_dict(saved_disk_infos, disk_info)

    print("Known disks now: ")
    for disk_info in saved_disk_infos.values():
        print_disk_info(disk_info)

    print("Saving stats...")
    save_stats(saved_disk_infos, stat_file)


@label_disks_cli.command("list")
def list_cli():
    stat_file = get_statfile_path()
    print("Opening stat file at", stat_file)
    saved_disk_infos = load_stats(stat_file)

    print("Known disks: ")
    for disk_info in saved_disk_infos.values():
        print_disk_info(disk_info)


Multido = str


def typeset_multido(title: str, subtitle: str, items: Iterable[str]) -> Multido:
    result = (
        r"\multido{}{2}{%"
        + "\n"
        + r"\begin{labelbox}{10cm}{5cm}{"
        + title
        + "}["
        + subtitle
        + "]\n"
    )
    for item in items:
        result += r"\item " + item + "\n"

    result += r"\end{labelbox}" + "\n" + r"}" + "\n"
    return result


def typeset_document(*multido: Multido):
    return (
        r"\documentclass[a4paper]{labeldoc}"
        + "\n"
        + r"\usepackage{multido}"
        + "\n"
        + "\n"
        + r"\renewcommand{\labeldoctitlesize}{\large}"
        + "\n"
        + r"\renewcommand{\labeldocsubtitlesize}{\large}"
        + "\n"
        + r"\begin{document}"
        + "\n"
        + "\n".join(multido)
        + "\n"
        + r"\end{document}"
        + "\n"
    )


@label_disks_cli.command("typeset")
def list_typeset_labels():
    stat_file = get_statfile_path()
    print("Opening stat file at", stat_file)
    saved_disk_infos = load_stats(stat_file)

    print("Known disks: ")
    for disk_info in saved_disk_infos.values():
        outfile = Path(disk_info.model + "_-_" + disk_info.serial + ".tex")
        print("Writing: " + str(outfile))
        items = [
            "Volume: " + volume for volume in ensure_iterator(disk_info.volume_group)
        ] + ["Content: " + content for content in ensure_iterator(disk_info.content)]
        a_multido = typeset_multido(disk_info.model, disk_info.serial, items)
        with outfile.open("w", **UTF8) as outstream:
            outstream.write(typeset_document(a_multido))


@label_disks_cli.command("writeout-labeldoc.cls")
def writeout_labeldoc():
    with (
        pkg_resources.files(resources).joinpath("labeldoc.cls").open("rb") as f,
        open("labeldoc.cls", "wb") as g,
    ):
        g.write(f.read())
