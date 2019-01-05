"""
Build functions
"""
from distutils.dir_util import copy_tree, remove_tree
from subprocess import call


def _run_command(shell_command):
    """
    Run shell command
    :param shell_command: shell command string with all arguments
    :return: result of run
    """
    return call(shell_command, shell=True)


def _get_build_path(path):
    """
    Get path to build folder
    :param path: src folder path
    :return: build folder path
    """
    return "{}.pyex".format(path)


def build_clean(path):
    """
    Remove prepped build folder
    :param path: src folder path
    """
    build_path = _get_build_path(path)
    try:
        remove_tree(build_path)
    except FileNotFoundError:
        pass


def build_prep(path):
    """
    Prep build folder for zipping
    :param path: src folder path
    """
    build_clean(path)
    build_path = _get_build_path(path)
    copy_tree(path, build_path)


def build_requirements(path):
    """
    Install requirements into build folder
    :param path: src folder path
    """
    build_path = _get_build_path(path)
    install_cmd = (
        "pip install"
        " --install-option='--prefix={}'"
        " --ignore-installed"
        " -r '{}/requirements.txt'"
    ).format(build_path, path)
    _run_command(install_cmd)


def build_compile(path):
    """
    Compile all python source files in build directory
    :param path: src folder path
    """
    build_path = _get_build_path(path)
    _run_command("python -m compileall {}".format(build_path))
    _run_command("find {} -name '*.py' -type f -delete".format(build_path))


def run(args):
    """
    Run build using arguments
    :param args: dict
    """
    src_path = args.path[0]
    build_prep(src_path)
    if args.install:
        build_requirements(src_path)

    # zip folder
    # write shebang
    # add executable bit
