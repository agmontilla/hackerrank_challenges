""" Test Validating UID Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.validating_uid import UUIDCollection, main


class TestUID:
    """Test Validating UID module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = ["2", "B1CD102354", "B1CDEF2354"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "Invalid\nValid\n"

    def test_valid_uid(self) -> None:
        """Test valid UID"""
        uuids = ["B1CD102354", "B1CDEF2354"]
        assert list(UUIDCollection(uuids).are_valid()) == ["Invalid", "Valid"]
