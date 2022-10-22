from pytest import CaptureFixture
from python.regex_and_parsing.detect_tags_attributes import MyHTMLParser


class TestDetectTagsAttributes():
    def test_detect_tags_attributes(self, capfd: CaptureFixture) -> None:
        html = """<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>"""

        expected = (
            "head\n"
            "title\n"
            "object\n"
            "-> type > application/x-flash\n"
            "-> data > your-file.swf\n"
            "-> width > 0\n"
            "-> height > 0\n"
            "param\n"
            "-> name > quality\n"
            "-> value > high\n"
        )

        parser = MyHTMLParser()
        parser.feed(html)
        out, _ = capfd.readouterr()
        assert out == expected
