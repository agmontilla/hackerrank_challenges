from python.strings.find_a_string import count_substring


class TestFindAString():

    def test_count_substring(self) -> None:
        assert count_substring('ABCDCDC', 'CDC') == 2
