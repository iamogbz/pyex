"""
Test build module
"""
from glob import glob
from os import path, remove
import subprocess

from build import (
    build_clean,
    build_compile,
    build_prep,
    build_requirements,
    run,
)


class MockObject:
    pass

class TestBuild:
    """
    Build tests
    """

    app_path = path.abspath('./src/__tests__/mock_app')
    build_path = '{}.pyex'.format(app_path)
    zip_path = '{}.zip'.format(build_path)
    output_path = '{}.ex'.format(app_path)
    main_file = '__main__.py'
    ignore_file = 'mock.ignore'
    args = MockObject()
    args.path = [app_path]
    args.ignore = []
    args.install = True
    args.output = [output_path]

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
        assert path.exists(path.join(self.build_path, self.main_file)) is True
        assert (
            path.exists(path.join(self.build_path, self.ignore_file)) is False
        )

    def _build_reprep(self):
        build_clean(self.app_path)
        build_prep(self.app_path, [])

    def test_build_requirements_installs_into_target(self):
        """
        Test build requirements install requirements.txt to build folder
        """
        self._build_reprep()
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
        self._build_reprep()
        build_compile(self.app_path)
        file_glob = "__main__*.pyc"
        py2_files = glob(path.join(self.build_path, file_glob))
        py3_files = glob(path.join(self.build_path, "**", file_glob))
        assert py2_files or py3_files

    def test_build_run_creates_python_executable(self):
        """
        Test build run successfully creates runnable
        """
        run(self.args)
        assert path.exists(self.zip_path) is False
        assert (
            subprocess.check_output(
                self.output_path, shell=True, cwd=self.app_path
            )
        ) == b"Good News, Bad News\n"

    def test_run_does_not_install_requirements_before_building(self, mocker):
        """
        Test run build does not install requirements and builds exec
        """
        mock_build_req = mocker.patch('build.build_requirements')
        if path.exists(self.output_path):
            remove(self.output_path)
        self.args.install = False
        run(self.args)
        mock_build_req.assert_not_called()
        assert path.exists(self.zip_path) is False
        assert path.exists(self.output_path) is True
        remove(self.output_path)
