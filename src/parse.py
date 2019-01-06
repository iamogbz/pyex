"""
Argument parsing
"""
import argparse


def add_options(*, parser):
    """
    Add parser options
    :param parser: ArgumentParser
    """
    parser.add_argument(
        "path",
        type=str,
        nargs=1,
        help="path to the python script (folder with __main__.py entry point)",
    )
    parser.add_argument(
        "-O",
        "--output",
        type=str,
        nargs=1,
        required=True,
        help="filename of built executable",
    )
    parser.add_argument(
        "-I",
        "--install",
        action="store_true",
        help="install requirements.txt and include in executable",
    )
    parser.add_argument(
        "-G",
        "--ignore",
        nargs="*",
        default=[],
        help="glob pattern of src files to ignore",
    )


def args():
    """
    Get arguments
    :return: dictionary of arguments
    """
    parser = argparse.ArgumentParser(description="Build python executable")
    add_options(parser=parser)
    return parser.parse_args()
