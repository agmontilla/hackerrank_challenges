""" Test Find The Maximum Depth Challenge """
from xml.etree import ElementTree as etree

from pytest import CaptureFixture, MonkeyPatch

from challenges.xml.find_the_maximum_depth import depth, main


class TestFindTheMaximumDepth:
    """Test Find The Maximum Depth module"""

    def test_main(self, capsys: CaptureFixture, monkeypatch: MonkeyPatch) -> None:
        """Test main function"""
        inputs = [
            "6",
            "<feed xml:lang='en'>",
            "    <title>HackerRank</title>",
            "    <subtitle lang='en'>Programming challenges</subtitle>",
            "    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>",
            "    <updated>2013-12-25T12:00:00</updated>",
            "</feed>",
        ]
        monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
        main()
        captured = capsys.readouterr()
        assert captured.out == "1\n"

    def test_depth(self) -> None:
        """Test depth function"""
        xml = "<feed xml:lang='en'><title>HackerRank</title></feed>"
        tree = etree.ElementTree(etree.fromstring(xml))
        assert depth(tree.getroot(), -1) == 1
