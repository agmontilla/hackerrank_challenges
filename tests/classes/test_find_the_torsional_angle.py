""" Test FindTheTorsionalAngle Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.classes.find_the_torsional_angle import Points, main


class TestFindTheTorsionalAngle:
    """Test FindTheTorsionalAngle module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        input_values = ["0 4 5", "1 7 6", "0 5 9", "1 7 2"]
        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "8.19\n"

    def test_sub_operation(self) -> None:
        """Test sub operation with Points"""
        a = Points(0, 4, 5)
        b = Points(1, 7, 6)
        results = a - b
        assert results.x == 1
        assert results.y == 3
        assert results.z == 1

    def test_dot_operation(self) -> None:
        """Test dot operation with Points"""
        a = Points(0, 4, 5)
        b = Points(1, 7, 6)
        results = a.dot(b)
        assert results == 58

    def test_cross_operation(self) -> None:
        """Test cross operation with Points"""
        a = Points(0, 4, 5)
        b = Points(1, 7, 6)
        results = a.cross(b)
        assert results.x == -11
        assert results.y == 5
        assert results.z == -4

    def test_absolute_operation(self) -> None:
        """Test absolute operation with Points"""
        a = Points(0, 4, 5)
        results = a.absolute()
        assert results == 6.4031242374328485

    def test_str_operation(self) -> None:
        """Test str operation with Points"""
        a = Points(0, 4, 5)
        results = str(a)
        assert results == "0 4 5"
