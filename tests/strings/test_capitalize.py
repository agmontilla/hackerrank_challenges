from python.strings.capitalize import solve


class TestCapitalize():

    def test_capitalize_is_working(self) -> None:
        assert solve('hello world') == 'Hello World'
