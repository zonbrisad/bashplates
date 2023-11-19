#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
# program for columnizing a datastream
#
# File:     columnize
# Author:   Peter Malmberg  <peter.malmberg@gmail.com>
# Org:      __ORGANISTATION__
# Date:     2023-11-18
# License:
# Python:   >= 3.0
#
# ----------------------------------------------------------------------------

import math
import traceback
import os
import sys
import logging
import argparse
import re
import shutil


# https://stackoverflow.com/questions/17658512/how-to-pipe-input-to-python-line-by-line-from-linux-program
# https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python


class App:
    NAME = "columnize"
    VERSION = "0.01"
    DESCRIPTION = "Program for columnizing datastreams"
    LICENSE = ""
    AUTHOR = "Peter Malmberg"
    EMAIL = "<peter.malmberg@gmail.com>"
    ORG = "__ORGANISATION__"
    HOME = ""
    ICON = ""


ansi_regex = (
    r"\x1b("
    r"(\[\??\d+[hl])|"
    r"([=<>a-kzNM78])|"
    r"([\(\)][a-b0-2])|"
    r"(\[\d{0,2}[ma-dgkjqi])|"
    r"(\[\d+;\d+[hfy]?)|"
    r"(\[;?[hf])|"
    r"(#[3-68])|"
    r"([01356]n)|"
    r"(O[mlnp-z]?)|"
    r"(/Z)|"
    r"(\d+)|"
    r"(\[\?\d;\d0c)|"
    r"(\d;\dR))"
)
ansi_escape1 = re.compile(ansi_regex, flags=re.IGNORECASE)


ansi_escape2 = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")


def main() -> None:
    logging_format = "[%(levelname)s] %(lineno)-4d %(funcName)-14s : %(message)s"

    parser = argparse.ArgumentParser(
        prog=App.NAME, description=App.DESCRIPTION, epilog="", add_help=True
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{App.NAME} {App.VERSION}",
        help="Print version information",
    )

    parser.add_argument(
        "--debug", action="store_true", default=False, help="Print debug messages"
    )
    parser.add_argument(
        "--truncate", action="store_true", default=False, help="Truncate long lines"
    )
    parser.add_argument(
        "--columns", action="store", type=int, default=2, help="Number of columns"
    )

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(format=logging_format, level=logging.DEBUG)

    cols, rows = shutil.get_terminal_size()
    col_width = cols // args.columns

    lines = []
    while True:
        try:
            line = input()
            if args.truncate is True:
                if len(line) > col_width:
                    line = line[0:col_width]
            lines.append(line)
        except EOFError:
            break

    lnr = len(lines)
    lpc = math.ceil(lnr / args.columns)

    # slice rows into columns
    columns = []
    for i in range(0, args.columns):
        col = lines[(i * lpc) : ((i * lpc) + lpc)]
        columns.append(col)

    for c in zip(*columns):
        for line in c:
            eline = ansi_escape2.sub("", line)
            pad = (col_width - len(eline)) * " "
            print(f"{line}{pad}", end="")

        print()  # newline


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print("ERROR, UNEXPECTED EXCEPTION")
        print(str(e))
        traceback.print_exc()
        os._exit(1)
