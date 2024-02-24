""" Test cases for discard_remove_pop module """

from pytest import CaptureFixture, MonkeyPatch

from challenges.sets.discard_remove_pop import main, run_discard_remove_pop


class TestDiscardRemovePop:
    """Test cases for discard_remove_pop function"""

    def test_discard_remove_pop_operation_is_working_as_expected(self, monkeypatch: MonkeyPatch) -> None:
        """discard_remove_pop operation is working as expected"""
        # Arrange
        set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        operations = 2
        inputs = ["pop", "remove 9"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        # Act
        results = run_discard_remove_pop(set_a, operations)
        # Assert
        assert results == {2, 3, 4, 5, 6, 7, 8}

    def test_print_discard_remove_pop_operation(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """print discard_remove_pop operation is working as expected"""
        inputs = [
            "9",
            "1 2 3 4 5 6 7 8 9",
            "10",
            "pop",
            "remove 9",
            "discard 9",
            "discard 8",
            "remove 7",
            "pop",
            "discard 6",
            "remove 5",
            "pop",
            "discard 5",
        ]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "4\n"
