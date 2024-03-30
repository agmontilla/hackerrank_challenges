""" Default Arguments Challenge """
from abc import ABC, abstractmethod


class Stream(ABC):
    """Abstract class for streams"""

    @abstractmethod
    def get_next(self) -> int:
        """Get the next value from the stream"""


class EvenStream(Stream):
    """Stream of even numbers"""

    def __init__(self) -> None:
        self.current = 0

    def get_next(self) -> int:
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(Stream):
    """Stream of odd numbers"""

    def __init__(self) -> None:
        self.current = 1

    def get_next(self) -> int:
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n: int, stream: Stream | None = None) -> None:
    """Print the next n values from the stream"""
    if not stream:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


def main() -> None:
    """Main function"""
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        number = int(n)
        if stream_name == "even":
            print_from_stream(number)
        else:
            print_from_stream(number, OddStream())


if __name__ == "__main__":
    main()
