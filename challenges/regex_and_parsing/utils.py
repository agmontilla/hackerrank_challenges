""" Regex and Parsing Utils """
from typing import List


class Reader:
    """Reader"""

    MAX_LINES = 100

    def readlines(self) -> List[str]:
        """Read lines"""
        number_of_lines = int(input())
        if number_of_lines > self.MAX_LINES:
            raise ValueError("Number of lines is too big")
        lines = []
        for _ in range(number_of_lines):
            lines.append(input())
        return lines


class MatrixReader:
    """Matrix Reader"""

    def readlines(self) -> List[str]:
        """Read lines"""
        n, _ = map(int, input().split())
        matrix = []

        for _ in range(n):
            row = input()
            matrix.append(row)

        return matrix
