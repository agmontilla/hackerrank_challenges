""" Deque operations Challenge """

from collections import deque
from typing import Deque


def run_deque_operations(operations: list[str]) -> Deque:
    """Run the deque operations"""
    queue: Deque = deque()
    for operation in operations:
        data = operation.split()
        _ = getattr(queue, data[0])(int(data[1])) if len(data) > 1 else getattr(queue, data[0])()

    return queue


def main() -> None:
    """Main function"""

    number_of_operations = int(input())
    operations = [input() for _ in range(number_of_operations)]

    queue = run_deque_operations(operations)

    print(*queue)


if __name__ == "__main__":
    main()
