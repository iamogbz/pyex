"""
Pyex main entry
"""
import argparse

from build import build_prep, build_requirements


def add_options(parser):
    """
    Add parser options
    :param parser: ArgumentParser
    """
    parser.add_argument(
        "path",
        type=str,
        nargs=1,
        help="Path to the python script (folder with __main__.py entry point)",
    )
    parser.add_argument(
        "--install",
        "-I",
        action="store_true",
        help="Should install requirements.txt in folder",
    )


def main():
    """
    Run main code
    """
    parser = argparse.ArgumentParser(description="Build python executable")
    add_options(parser)
    args = parser.parse_args()
    src_path = args.path[0]
    build_prep(src_path)
    if args.install:
        build_requirements(src_path)

    # zip folder
    # write shebang
    # add executable bit


main()
