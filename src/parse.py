"""
Argument parsing
"""
import argparse


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


def args():
    """
    Get arguments
    :return: dictionary of arguments
    """
    parser = argparse.ArgumentParser(description="Build python executable")
    add_options(parser)
    return parser.parse_args()
