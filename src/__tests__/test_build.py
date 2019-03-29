"""
Test build module
"""
import build


class TestBuild:
    """
    Build tests
    """

    def test_build_clean_removes_build_path(self):
        """
        Test build clean removes previous build path
        """
        pass

    def test_build_clean_does_not_fail_if_path_does_not_exist(self):
        """
        Test build clean with build folder not exisiting does not fail
        """
        pass

    def test_build_prep_sets_up_folder_correctly(self):
        """
        Test build prep copies src to build folder, ignoring specified files.
        """
        pass

    def test_build_requirements_installs_into_target(self):
        """
        Test build requirements install requirements.txt to build folder
        """
        pass

    def test_build_compile_creates_pyc_for_src(self):
        """
        Test that build compile command creates python executable
        """
        pass

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
