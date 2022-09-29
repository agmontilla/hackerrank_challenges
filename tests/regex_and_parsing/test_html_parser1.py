from pytest import CaptureFixture
from python.regex_and_parsing.html_parser1 import MyHTMLParser


class TestHTMLParser1:
    def test_html_parser1(self, capfd: CaptureFixture) -> None:
        html = """<html><head><title>HTML Parser - I</title></head>
        <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
        """
        expected = (
            "Start : html\n"
            "Start : head\n"
            "Start : title\n"
            "End   : title\n"
            "End   : head\n"
            "Start : body\n"
            "-> data-modal-target > None\n"
            "-> class > 1\n"
            "Start : h1\n"
            "End   : h1\n"
            "Empty : br\n"
            "End   : body\n"
            "End   : html\n"
        )

        parser = MyHTMLParser()
        parser.feed(html)
        out, _ = capfd.readouterr()
        assert out == expected
