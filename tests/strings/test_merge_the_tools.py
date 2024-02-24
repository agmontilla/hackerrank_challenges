""" Test cases for MergeTheTools """
import pytest
from pytest import CaptureFixture

from python.strings.merge_the_tools import MergeTheTools


class TestMergeTheTools:
    """Test cases for MergeTheTools"""

    def test_merge_the_tools_is_working_as_expected(self, capsys: CaptureFixture) -> None:
        """MergeTheTools is working as expected"""
        MergeTheTools("AABCAAADA", 3).run()
        captured = capsys.readouterr()
        assert captured.out == "AB\nCA\nAD\n"

    def test_merge_the_tools_is_raising_value_error(self) -> None:
        """MergeTheTools is raising ValueError when K is not a factor of length of the string"""
        with pytest.raises(ValueError, match="K is not a factor of length of the string"):
            MergeTheTools("AABCAAADA", 4).run()
