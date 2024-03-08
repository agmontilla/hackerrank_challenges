"""" Test RegexSubstitution class """

from pytest import CaptureFixture, MonkeyPatch

from challenges.regex_and_parsing.regex_substitution import RegexSubstitution, main


class TestRegexSubstitution:
    """RegexSubstitution test class"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test run function"""
        inputs = [
            "11",
            "a = 1;",
            "b = input();",
            "",
            "if a + b > 0 && a - b < 0:",
            "    start()",
            "elif a*b > 10 || a/b < 1:",
            "    stop()",
            "print set(list(a)) | set(list(b)) ",
            "#Note do not change &&& or ||| or & or |",
            "#Only change those '&&' which have space on both sides.",
            "#Only change those '|| which have space on both sides.",
        ]
        output = [
            "a = 1;",
            "b = input();",
            "",
            "if a + b > 0 and a - b < 0:",
            "    start()",
            "elif a*b > 10 or a/b < 1:",
            "    stop()",
            "print set(list(a)) | set(list(b)) ",
            "#Note do not change &&& or ||| or & or |",
            "#Only change those '&&' which have space on both sides.",
            "#Only change those '|| which have space on both sides.",
        ]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

        main()
        captured = capsys.readouterr()
        assert captured.out == "\n".join(output) + "\n"

    def test_replace(self) -> None:
        """Test replace function"""
        text = ["&& || || && && ||"]
        expected = ["&& or or and and ||"]
        regex_substitution = RegexSubstitution(text)
        result = regex_substitution.replace()
        assert result == expected
