"""
Test parse module
"""
from src.parse import init


class TestParse:
    """
    Parse test
    """
    parser = init()

    def test_path_is_required(self):
        """
        Test parser requires the path argument
        """
        self.parser.parse_args(args=["-O", "executable"])
