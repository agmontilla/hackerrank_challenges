""" Test Eye and Identity Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.eye_and_identity import generate_eye, main


class TestEyeAndIdentity:
    """Test Eye and Identity Challenge"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs: list[str] = ["3 3\n"]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        output = "[[ 1.  0.  0.]\n [ 0.  1.  0.]\n [ 0.  0.  1.]]\n"
        assert captured.out == output

    def test_generate_eye(self) -> None:
        """Test generate_eye function"""
        assert generate_eye(3, 3).tolist() == [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        assert generate_eye(2, 2).tolist() == [[1.0, 0.0], [0.0, 1.0]]
        assert generate_eye(1, 1).tolist() == [[1.0]]
