""" Test Hex Color Challenge """
from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.hex_color import Text, main


class TestHexColor:
    """Test Hex Color module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = [
            "11",
            "#BED",
            "{",
            "color: #FfFdF8; background-color:#aef;",
            "font-size: 123px;",
            "background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
            "}",
            "#Cab",
            "{",
            "background-color: #ABC;",
            "border: 2px dashed #fff;",
            "}",
        ]

        expected_output = "#FfFdF8\n#aef\n#f9f9f9\n#fff\n#ABC\n#fff\n"

        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output

    def test_get_hex_codes(self) -> None:
        """Test get_hex_codes method"""
        text = Text(
            [
                "#BED",
                "{",
                "color: #FfFdF8; background-color:#aef;",
                "font-size: 123px;",
                "background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
                "}",
                "#Cab",
                "{",
                "background-color: #ABC;",
                "border: 2px dashed #fff;",
                "}",
            ]
        )

        assert list(text.get_hex_codes()) == ["#FfFdF8", "#aef", "#f9f9f9", "#fff", "#ABC", "#fff"]
