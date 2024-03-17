""" Test for Name Directory Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.closures_and_decorators.name_directory import (
    Person,
    main,
    name_format,
    person_lister,
)


class TestNameDirectory:
    """Test Name Directory Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = ["3", "Mike Thomson 20 M", "Robert Bustle 32 M", "Andria Bustle 30 F"]
        expected_outputs = "Mr. Mike Thomson\nMs. Andria Bustle\nMr. Robert Bustle\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_name_format(self) -> None:
        """Test name_format function is working as expected"""

        person = ("Mike", "Thomson", "20", "M")
        assert name_format(person) == "Mr. Mike Thomson"

    def test_person_lister(self) -> None:
        """Test person_lister function is working as expected"""

        @person_lister
        def to_be_decorate(person: Person) -> str:
            return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

        people = [
            ("Mike", "Thomson", "20", "M"),
            ("Robert", "Bustle", "32", "M"),
            ("Andria", "Bustle", "30", "F"),
        ]
        expected_output = ["Mr. Mike Thomson", "Ms. Andria Bustle", "Mr. Robert Bustle"]
        assert list(to_be_decorate(people)) == expected_output
