""" Tests for the Hello World challenge """

from pytest import CaptureFixture

from challenges.introduction.hello_world import main


class TestHelloWorld:
    """Tests for the Hello World module"""

    def test_hello_world(self, capsys: CaptureFixture) -> None:
        """Test the main program of hello world is working as expected"""
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello, World!"
