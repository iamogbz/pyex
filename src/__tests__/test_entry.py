"""
Test main entry
"""
import parse
import build
import entry


class MockMethod:
    """
    Records last call
    """

    def __init__(self):
        self.args = []
        self.kwargs = {}

    def __call__(self, *args, **kwargs):
        print("test")
        self.args = args
        self.kwargs = kwargs


def test_build_run_is_on_parse_args(monkeypatch):
    """
    Test build run is called with parsed args from main
    """
    mock_build_run = MockMethod()
    monkeypatch.setattr(build, "run", mock_build_run)
    mock_parsed_args = ["arg1", "arg2"]
    monkeypatch.setattr(parse, "args", lambda: mock_parsed_args)
    entry.main()
    assert mock_build_run.kwargs == {"args": mock_parsed_args}
