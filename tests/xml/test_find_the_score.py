""" Test cases for Find the Score challenge """
from xml.etree import ElementTree as etree

from pytest import CaptureFixture, MonkeyPatch

from challenges.xml.find_the_score import get_attr_number, main


class TestFindTheScore:
    """Test cases for Find the Score challenge"""

    def test_main(self, capfd: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        xml = "<feed xml:lang='en'>\n\
            <title>HackerRank</title>\n\
            <subtitle lang='en'>Programming challenges</subtitle>\n\
            <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\n\
            <updated>2013-12-25T12:00:00</updated>\n\
            </feed>\n\
        "

        monkeypatch.setattr("sys.stdin.readline", lambda: "6\n")
        monkeypatch.setattr("sys.stdin.read", lambda: xml)
        expected = "5\n"
        main()
        out, _ = capfd.readouterr()
        assert out == expected

    def test_get_attr_number(self) -> None:
        """Test get_attr_number function"""
        xml = "<feed xml:lang='en'>\n\
            <title>HackerRank</title>\n\
            <subtitle lang='en'>Programming challenges</subtitle>\n\
            <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\n\
            <updated>2013-12-25T12:00:00</updated>\n\
            </feed>\n\
        "
        tree = etree.ElementTree(etree.fromstring(xml))
        root = tree.getroot()
        assert get_attr_number(root) == 5
