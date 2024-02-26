""" Test for the Python List challenge."""
from pytest import CaptureFixture, MonkeyPatch

from challenges.basic_data_types.python_list import main, run_option


class TestPythonList:
    """Test for the Python List challenge."""

    def test_run_option(self) -> None:
        """Test for the function run_option is working as expected."""
        data: list[int] = []
        run_option("insert", data, [0, 5])
        run_option("insert", data, [1, 10])
        run_option("insert", data, [0, 6])
        expected = [6, 5, 10]

        assert data == expected

    def test_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function is working as expected."""

        input_values = [
            "12",
            "insert 0 5",
            "insert 1 10",
            "insert 0 6",
            "print",
            "remove 6",
            "append 9",
            "append 1",
            "sort",
            "print",
            "pop",
            "reverse",
            "print",
        ]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected = "[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n"

        main()

        out, _ = capsys.readouterr()
        assert out == expected
