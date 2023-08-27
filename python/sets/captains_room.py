from collections import Counter
from typing import List


class CaptainRoom:

    def __init__(self, room_numbers: List[int]) -> None:
        self.room_numbers = room_numbers

    def get_captain_room_number(self) -> int:
        captain_number = Counter(self.room_numbers).most_common()[-1][0]
        return int(captain_number)


def main() -> None:
    _ = int(input())
    room_numbers = sorted(list(map(int, input().split())))

    captain_room = CaptainRoom(room_numbers)
    print(captain_room.get_captain_room_number())


if __name__ == "__main__":
    main()
