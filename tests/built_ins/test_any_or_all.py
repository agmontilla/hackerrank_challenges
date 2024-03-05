""" Test Any or All challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.built_ins.any_or_all import all_positive, is_palindrome, main


class TestAnyOrAll:
    """Test Any or All module"""

    @mark.parametrize(
        "data, expected",
        [
            (121, True),
            (123, False),
        ],
    )
    def test_is_palindrome(self, data: int, expected: bool) -> None:
        """Test is_palindrome function is working as expected"""
        assert is_palindrome(data) == expected

    @mark.parametrize(
        "data, expected",
        [
            ([1, 2, 3, 4, 5], True),
            ([1, 2, 3, 4, -5], False),
        ],
    )
    def test_all_positive(self, data: list[int], expected: bool) -> None:
        """Test all_positive function is working as expected"""
        assert all_positive(data) == expected

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["5", "12 9 61 5 14"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "True\n"
