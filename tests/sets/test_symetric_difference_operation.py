""" Test Symetric Difference Operation """

from pytest import CaptureFixture, MonkeyPatch

from challenges.sets.symetric_difference_operation import get_symetric_difference, main


class TestSymetricDifferenceOperation:
    """Test Symetric Difference Operation"""

    def test_symetric_difference_operation_is_working(self) -> None:
        """Symetric difference operation is working as expected"""
        english_students = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        french_students = {10, 1, 2, 3, 11, 21, 55, 6, 8}

        result = get_symetric_difference(english_students, french_students)

        assert result == 8

    def test_symetric_difference_main_program_is_working(self, capfd: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Symetric difference main program is working as expected"""

        inputs = ["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()

        out, _ = capfd.readouterr()
        assert out == "8\n"
