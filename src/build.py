"""
Build functions
https://docs.python.org/3.7/library/shutil.html
"""
from shutil import copytree, ignore_patterns, make_archive, rmtree
import subprocess


def _run(shell_command):
    """
    Run shell command
    :param shell_command: shell command string with all arguments
    :return: result of run
    """
    return subprocess.check_output(shell_command, shell=True)


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
    build_path = _get_build_path(path=path)
    try:
        rmtree(build_path)
    except OSError:
        pass


def build_prep(path, ignore):
    """
    Prep build folder for zipping
    :param path: src folder path
    """
    build_clean(path=path)
    build_path = _get_build_path(path=path)
    copytree(path, build_path, ignore=ignore_patterns(*ignore))


def build_requirements(path):
    """
    Install requirements into build folder
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    install_cmd = (
        "pip install --target='{}' --upgrade -r '{}/requirements.txt'"
    ).format(build_path, path)
    _run(shell_command=install_cmd)


def build_compile(path):
    """
    Compile all python source files in build directory
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    _run(shell_command="python -m compileall {}".format(build_path))
    _run(
        shell_command="find {} -name '*.py' -type f -delete".format(build_path)
    )


def build_zip(path):
    """
    Compress distributable into a zip file
    :param path: src folder path
    """
    build_path = _get_build_path(path=path)
    make_archive(base_name=build_path, format="zip", root_dir=build_path)


def build_exec(src_path, dest_path):
    """
    Build executable from archive file
    :param src_path: src folder path
    :param dest_path: executable file
    """
    shebang = "#!/usr/bin/env python"
    zip_file = "{}.zip".format(_get_build_path(path=src_path))
    shell_cmd = (
        "echo '{shebang}' > {executable} && "
        "cat {archive} >> {executable} && "
        "chmod +x {executable} && rm {archive}"
    ).format(archive=zip_file, executable=dest_path, shebang=shebang)
    _run(shell_command=shell_cmd)


def run(args):
    """
    Run build using arguments
    :param args: parsed arguments object
    """
    src_path = args.path[0]
    build_prep(path=src_path, ignore=args.ignore)
    if args.install:
        build_requirements(path=src_path)

    build_zip(path=src_path)
    build_exec(src_path=src_path, dest_path=args.output[0])
    build_clean(path=src_path)
