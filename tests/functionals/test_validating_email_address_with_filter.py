""" Test cases for Validating Email Address with a Filter Challenge """

from pytest import CaptureFixture, MonkeyPatch, mark

from challenges.functionals.validating_email_address_with_filter import (
    filter_mail,
    fun,
    main,
)


class TestValidatingEmailAddressWithFilter:
    """Test Validating Email Address with a Filter module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        input_values = ["3", "lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]
        output = ["['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']\n"]

        monkeypatch.setattr("builtins.input", lambda: input_values.pop(0))
        main()

        captured = capsys.readouterr()
        assert captured.out == "".join(output)

    @mark.parametrize(
        "emails, expected",
        [
            ("lara@hackerrank.com", True),
            ("liz.9@hackerrank.com", False),
        ],
    )
    def test_fun(self, emails: str, expected: bool) -> None:
        """Test fun function"""
        assert fun(emails) == expected

    def test_filter_mail(self) -> None:
        """Test filter_mail function"""
        emails = ["lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]
        output = ["lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]

        results = filter_mail(emails)

        assert results == output
        assert isinstance(results, list)
