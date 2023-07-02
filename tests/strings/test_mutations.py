from python.strings.mutations import mutate_string


class TestMutations():

    def test_mutations_is_working_as_expected(self) -> None:
        assert mutate_string('abracadabra', 5, 'k') == 'abrackdabra'
