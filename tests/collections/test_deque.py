""" Test cases for deque Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.collections.deque import main, run_deque_operations


class TestDeque:
    """Test Deque module"""

    def test_run_deque_operations(self) -> None:
        """Test run_deque_operations function is working as expected"""
        operations = ["append 1", "append 2", "append 3", "appendleft 4", "pop", "popleft"]
        expected = [1, 2]
        assert list(run_deque_operations(operations)) == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = ["6", "append 1", "append 2", "append 3", "appendleft 4", "pop", "popleft"]
        output = "1 2\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == output
