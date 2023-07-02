from python.strings.split_and_join import split_and_join


class TestSplitAndJoin():

    def test_split_and_join_is_working_as_expected(self) -> None:
        assert split_and_join('this is a string') == 'this-is-a-string'
