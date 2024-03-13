"""Test Standarize Mobile Number Using Decorators Challenge"""
from pytest import CaptureFixture, MonkeyPatch

from challenges.closures_and_decorators.standarize_mobile_number import (
    main,
    sort_phone,
    wrapper,
)


class TestStandarizeMobileNumber:
    """Test Standarize Mobile Number Using Decorators Module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function is working as expected"""
        inputs = ["3", "07895462130", "919875641230", "9195969878"]
        expected_outputs = "+91 78954 62130\n+91 91959 69878\n+91 98756 41230\n"
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_outputs

    def test_sort_phone(self, capsys: CaptureFixture) -> None:
        """Test sort_phone function is working as expected"""
        phone_numbers = ["07895462130", "919875641230", "9195969878"]
        expected_output = "+91 78954 62130\n+91 91959 69878\n+91 98756 41230\n"
        sort_phone(phone_numbers)
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_wrapper(self) -> None:
        """Test wrapper function is working as expected and the inner function is called
        I didn't know how to test the decorator. This was a helpful resource:
        https://medium.com/analytics-vidhya/testing-python-decorators-3c5777e4524d
        https://stackoverflow.com/questions/34648337/how-to-test-a-decorator-in-a-python-package
        """
        phone_numbers = ["07895462130", "919875641230", "9195969878"]

        @wrapper
        def to_be_decorated(phone_numbers: list[str]) -> None:
            assert list(phone_numbers) == ["+91 78954 62130", "+91 98756 41230", "+91 91959 69878"]

        to_be_decorated(phone_numbers)
