""" Regex and Parsing Utils """
from typing import List


class Reader():
    """ Reader """
    MAX_LINES = 100

    def readlines(self) -> List[str]:
        """ Read lines """
        number_of_lines = int(input())
        if number_of_lines > self.MAX_LINES:
            raise ValueError("Number of lines is too big")
        lines = []
        for _ in range(number_of_lines):
            lines.append(input())
        return lines
