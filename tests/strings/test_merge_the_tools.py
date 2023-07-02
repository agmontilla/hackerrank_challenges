import pytest
from pytest import CaptureFixture

from python.strings.merge_the_tools import MergeTheTools


class TestMergeTheTools:

    def test_merge_the_tools_is_working_as_expected(self, capsys: CaptureFixture) -> None:
        MergeTheTools('AABCAAADA', 3).run()
        captured = capsys.readouterr()
        assert captured.out == 'AB\nCA\nAD\n'

    def test_merge_the_tools_is_raising_value_error(self) -> None:
        with pytest.raises(ValueError, match="K is not a factor of length of the string"):
            MergeTheTools('AABCAAADA', 4).run()
