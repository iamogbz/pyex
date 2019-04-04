"""
Test build module
"""
from glob import glob
from os import path
import subprocess

from build import (
    build_clean,
    build_compile,
    build_exec,
    build_prep,
    build_requirements,
    build_zip,
)


class TestBuild:
    """
    Build tests
    """

    app_path = './src/__tests__/mock_app'
    build_path = '{}.pyex'.format(app_path)
    main_file = '__main__.py'
    ignore_file = 'mock.ignore'

    def test_build_clean_removes_build_path(self):
        """
        Test build clean removes previous build path
        """
        build_prep(self.app_path, [])
        assert path.exists(self.build_path) is True
        build_clean(self.app_path)
        assert path.exists(self.build_path) is False

    def test_build_clean_does_not_fail_if_path_does_not_exist(self):
        """
        Test build clean with build folder not exisiting does not fail
        """
        build_clean(self.app_path)
        assert path.exists(self.build_path) is False

    def test_build_prep_sets_up_folder_correctly(self):
        """
        Test build prep copies src to build folder, ignoring specified files.
        """
        build_clean(self.app_path)
        assert path.exists(self.build_path) is False
        build_prep(self.app_path, ['*.ignore'])
        assert path.exists(self.build_path) is True
        assert path.exists(path.join(self.build_path, self.main_file)) is True
        assert (
            path.exists(path.join(self.build_path, self.ignore_file)) is False
        )

    def test_build_requirements_installs_into_target(self):
        """
        Test build requirements install requirements.txt to build folder
        """
        build_clean(self.app_path)
        build_prep(self.app_path, [])
        build_requirements(self.app_path)
        assert (
            subprocess.check_output(
                "PYTHONPATH=. python .", shell=True, cwd=self.build_path
            )
        ) == b"Good News, Bad News\n"

    def test_build_compile_creates_pyc_for_src(self):
        """
        Test that build compile command creates python executable
        """
        build_clean(self.app_path)
        build_prep(self.app_path, [])
        build_compile(self.app_path)
        assert glob(path.join(self.build_path, "**", "__main__*.pyc"))

    def test_build_exec_creates_python_executable(self):
        """
        Test build exec successfully creates runnable
        """
        pass

    def test_run_installs_requirements_before_building(self):
        """
        Test run build installs requirements and builds exec
        """
        pass

    def test_run_calls_build_methods_order(self):
        """
        Test run build execution order
        """
        pass
