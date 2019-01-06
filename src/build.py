"""
Build functions
"""
from shutil import copytree, ignore_patterns, rmtree
from subprocess import call


def _run(*, shell_command):
    """
    Run shell command
    :param shell_command: shell command string with all arguments
    :return: result of run
    """
    return call(shell_command, shell=True)


def _get_build_path(*, path):
    """
    Get path to build folder
    :param path: src folder path
    :return: build folder path
    """
    return "{}.pyex".format(path)


def build_clean(*, path):
    """
    Remove prepped build folder
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    try:
        rmtree(build_path)
    except FileNotFoundError:
        pass


def build_prep(*, path, ignore=[]):
    """
    Prep build folder for zipping
    :param path: src folder path
    """
    build_clean(path=path)
    build_path = _get_build_path(path=path)
    copytree(path, build_path, ignore=ignore_patterns(*ignore))


def build_requirements(*, path):
    """
    Install requirements into build folder
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    install_cmd = (
        "pip install"
        " --install-option='--prefix={}'"
        " --ignore-installed"
        " -r '{}/requirements.txt'"
    ).format(build_path, path)
    _run(shell_command=install_cmd)


def build_compile(*, path):
    """
    Compile all python source files in build directory
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    _run(shell_command="python -m compileall {}".format(build_path))
    _run(shell_command="find {} -name '*.py' -type f -delete".format(build_path))


def build_zip(*, path):
    """
    Compress distributable into a zip file
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    make_archive(base_name=build_path, format="zip", root_dir=build_path)


def run(*, args):
    """
    Run build using arguments
    :param args: dict
    """
    src_path = args.path[0]
    build_prep(path=src_path, ignore=args.ignore)
    if args.install:
        build_requirements(path=src_path)

    build_zip(path=src_path)
    # write shebang
    # add executable bit
