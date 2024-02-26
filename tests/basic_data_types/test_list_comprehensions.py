"""Test for the List Comprehension challenge."""
from pytest import CaptureFixture, MonkeyPatch

from challenges.basic_data_types.list_comprehensions import (
    get_all_possible_cuboid_dim,
    main,
)


class TestListComprehension:
    """Test for the List Comprehension challenge."""

    def test_get_all_possible_cuboid_dim(self) -> None:
        """Test for the function get_all_possible_cuboid_dim is working as expected."""
        x = 1
        y = 1
        z = 1
        n = 2
        expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

        results = get_all_possible_cuboid_dim(x, y, z, n)

        assert results == expected

    def test_main_program_is_working(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test for the main function is working as expected."""

        input_values = ["1", "1", "1", "2"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        expected = "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n"

        main()

        out, _ = capsys.readouterr()
        assert out == expected
