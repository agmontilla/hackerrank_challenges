""" Test Zeros and Ones Challenge"""
from pytest import CaptureFixture, MonkeyPatch

from challenges.numpy.zeros_and_one import generate_ones, generate_zeros, main


class TestZerosAndOne:
    """Test Zeros and Ones Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = ["3 3"]
        expected_outputs = "[[0 0 0]\n [0 0 0]\n [0 0 0]]\n[[1 1 1]\n [1 1 1]\n [1 1 1]]\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_generate_zeros(self) -> None:
        """Test generate_zeros function is working as expected"""
        dimn = (2, 2)
        expected = [[0, 0], [0, 0]]
        assert generate_zeros(dimn).tolist() == expected

    def test_generate_ones(self) -> None:
        """Test generate_ones function is working as expected"""
        dimn = (2, 2)
        expected = [[1, 1], [1, 1]]
        assert generate_ones(dimn).tolist() == expected
