""" Test Cases for Mutations """

from pytest import CaptureFixture, MonkeyPatch

from python.sets.mutations import main, run_mutations


class TestMutations:
    """ Test Mutations """

    def test_run_mutations_is_working(self, monkeypatch: MonkeyPatch) -> None:
        """ Test run_mutations is working as expected """
        # Arrange
        inputs = [
            'intersection_update 10', '2 3 5 6 8 9 1 4 7 11',
            'update 2', '55 66',
            'symmetric_difference_update 5', '22 7 35 62 58',
            'difference_update 7', '11 22 35 55 58 62 66'
        ]
        monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

        # Act
        result = run_mutations(
            {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}, 4)

        # Assert
        assert result == 38

    def test_mutations_main_program(self, monkeypatch: MonkeyPatch, capfd: CaptureFixture) -> None:
        """ Test if mutation main program is working as expected """
        # Arrange
        inputs = [
            "16", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52", "4",
            "intersection_update 10", "2 3 5 6 8 9 1 4 7 11",
            "update 2", "55 66", "symmetric_difference_update 5", "22 7 35 62 58",
            "difference_update 7", "11 22 35 55 58 62 66"
        ]
        monkeypatch.setattr('builtins.input', lambda: inputs.pop(0))

        # Act
        main()

        # Assert
        out, _ = capfd.readouterr()
        assert out == "38\n"
