from pytest import CaptureFixture
from python.regex_and_parsing.html_parser2 import MyHTMLParser


class TestHTMLParser2:
    def test_html_parser2(self, capfd: CaptureFixture) -> None:
        html = """<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
"""

        expected = (
            ">>> Multi-line Comment\n"
            "[if IE 9]>IE9-specific content\n"
            "<![endif]\n"
            ">>> Data\n"
            " Welcome to HackerRank\n"
            ">>> Single-line Comment\n"
            "[if IE 9]>IE9-specific content<![endif]\n"
        )

        parser = MyHTMLParser()
        parser.feed(html)
        out, _ = capfd.readouterr()
        assert out == expected
