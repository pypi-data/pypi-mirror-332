#!/usr/bin/env python
"""
Convert Snakefile to rst file for auto documentation of workflows

Usage:
    smk_to_rst.py DIRECTORY [--stat]
    smk_to_rst.py (-h | --help)

Options:
    DIRECTORY      Base directory to be parsed
    --stat         Print summary about the digest process
    -h --help      Show this screen.

"""
from pathlib import Path
from smk2rst.docopt import docopt
from smk2rst import codebase_parser, print_stats


def main():
    args = docopt(__doc__)
    basepath = Path(args["DIRECTORY"])
    sources = codebase_parser(basepath)
    if args["--stat"]:
        print_stats(sources, basepath=basepath, show_details=True)


if __name__ == "__main__":
    main()
