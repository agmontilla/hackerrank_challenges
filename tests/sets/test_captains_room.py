""" Test cases for the captain room problem. """
from challenges.sets.captains_room import CaptainRoom


class TestCaptainRoom:
    """Test cases for CaptainRoom class."""

    def test_captain_room_is_working_as_expected(self) -> None:
        """Test that the captain room is working as expected."""
        inputs = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
        captain_room = CaptainRoom(inputs)
        assert captain_room.get_captain_room_number() == 8
