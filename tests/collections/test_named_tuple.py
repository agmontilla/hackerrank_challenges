""" Test cases for Named Tuple Challenge """
from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.collections.named_tuple import (
    Student,
    get_average_mark,
    main,
    process_inputs,
    transform_signature_fields,
)


class TestNamedTuple:
    """Test Named Tuple module"""

    def test_get_average_mark(self) -> None:
        """Test get_average_mark is working as expected"""
        students = [
            Student("1", "97", "Raymond", "7"),
            Student("2", "50", "Steven", "4"),
            Student("3", "91", "Adrian", "9"),
            Student("4", "72", "Stewart", "5"),
            Student("5", "80", "Peter", "6"),
        ]
        assert get_average_mark(students) == 78.00

    def test_process_inputs(self) -> None:
        """Test process_inputs is working as expected"""
        # Arrange
        fields = list(Student._fields)
        students = [
            "1 97 Raymond 7",
            "2 50 Steven 4",
            "3 91 Adrian 9",
            "4 72 Stewart 5",
            "5 80 Peter 6",
        ]

        expected = [
            Student("1", "97", "Raymond", "7"),
            Student("2", "50", "Steven", "4"),
            Student("3", "91", "Adrian", "9"),
            Student("4", "72", "Stewart", "5"),
            Student("5", "80", "Peter", "6"),
        ]

        # Act
        results = process_inputs(fields, students)

        # Assert
        assert results == expected

    def test_transform_signature_fields(self) -> None:
        """Test transform_signature_fields is working as expected"""
        # Arrange
        fields = ["ID", "MARKS", "NAME", "CLASS"]

        expected = ["id_", "marks_", "name_", "class_"]

        # Act
        results = transform_signature_fields(fields)

        # Assert
        assert results == expected

    @mark.parametrize(
        "input_values, expected",
        [
            (
                ["5", "ID MARKS NAME CLASS", "1 97 Raymond 7", "2 50 Steven 4", "3 91 Adrian 9", "4 72 Stewart 5", "5 80 Peter 6"],
                "78.00\n",
            ),
            (
                ["5", "MARKS CLASS NAME ID", "92 2 Calum 1", "82 5 Scott 2", "94 2 Jason 3", "55 8 Glenn 4", "82 2 Fergus 5"],
                "81.00\n",
            ),
        ],
    )
    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch, input_values: list[str], expected: str) -> None:
        """Test main is working as expected"""
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))

        main()

        captured = capsys.readouterr()
        assert captured.out == expected
