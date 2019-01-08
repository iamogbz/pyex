"""
Test parse module
"""
import argparse
import pytest
from src import parse


class TestParse:
    """
    Parse test
    """

    parser = parse.init()
    path_arg = "/path/to/folder"
    output_arg = "executable"
    required_args = [path_arg, "--output", output_arg]

    def test_path_is_required(self):
        """
        Test parser requires the path argument
        """
        with pytest.raises(SystemExit):
            self.parser.parse_args(args=["-O", "executable"])

    def test_path_accepts_only_one_arg(self):
        """
        Test parser accepts only one path argument
        """
        with pytest.raises(SystemExit):
            self.parser.parse_args(
                args=["/path/to/folder", "other/folder", "-O", "executable"]
            )

    def test_output_is_required(self):
        """
        Test parser requires output argument
        """
        with pytest.raises(SystemExit):
            self.parser.parse_args(args=["/path/to/folder"])

    def test_output_accepts_only_one_arg(self):
        """
        Test parser accepts only one output argument
        """
        with pytest.raises(SystemExit):
            self.parser.parse_args(
                args=["/path/to/folder", "-O", "executable", "other/executable"]
            )

    def test_accepts_required_args(self):
        """
        Test parser uses required arguments
        """
        args = self.parser.parse_args(self.required_args)
        assert args.path == [self.path_arg]
        assert args.output == [self.output_arg]

    def test_install_arg_defaults_to_false(self):
        """
        Test parser default install arg is false
        """
        args = self.parser.parse_args(self.required_args)
        assert not args.install

    def test_accepts_install_arg(self):
        """
        Test parser accepts install arg
        """
        input_args = self.required_args + ["-I"]
        args = self.parser.parse_args(input_args)
        assert args.install

        input_args = self.required_args + ["--install"]
        args = self.parser.parse_args(input_args)
        assert args.install

    def test_ignore_arg_defaults_to_empty_list(self):
        """
        Test parser default install arg is false
        """
        args = self.parser.parse_args(self.required_args)
        assert args.ignore == []

    def test_ignore_accepts_multiple_args(self):
        """
        Test parser accepts install arg
        """
        ignore_flags = ["*ignoreme", "__DO_NOT_INCLUDE_ME__"]
        input_args = self.required_args + ["-G"] + ignore_flags
        args = self.parser.parse_args(input_args)
        assert args.ignore == ignore_flags

        input_args = self.required_args + ["--ignore"] + ignore_flags
        args = self.parser.parse_args(input_args)
        assert args.ignore == ignore_flags


def test_calls_parse_args_on_init(monkeypatch):
    """
    Test parse.args uses initialised parser to get args
    """
    mock_parsed_args = ["mockReturn", "argValues"]
    mock_arg_parser = argparse.ArgumentParser("Mock Argument Parser")
    setattr(mock_arg_parser, "parse_args", lambda: mock_parsed_args)
    monkeypatch.setattr(parse, "init", lambda: mock_arg_parser)
    assert parse.args() == mock_parsed_args
