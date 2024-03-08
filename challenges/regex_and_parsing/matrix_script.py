""" Matrix Script """

import re
from typing import List

from .utils import MatrixReader


class MatrixScript:
    """MatrixScript"""

    REGEX_PATTERN = r"(?<=[a-zA-Z0-9])[\W_]+(?=[a-zA-Z0-9])"

    def __init__(self, matrix: List[str]) -> None:
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def get_message(self) -> str:
        """Get the message"""

        # Combine all the rows of the matrix into a single string
        message = "".join([self.matrix[i][j] for j in range(self.m) for i in range(self.n)])

        # Remove all the symbols from the message using regular expressions
        message = re.sub(self.REGEX_PATTERN, " ", message)
        return message


def main() -> None:
    """Main function"""
    reader = MatrixReader()
    matrix = reader.readlines()
    matrix_script = MatrixScript(matrix)
    print(matrix_script.get_message(), end="")


# Rememeber, in hackerrank, you need to remove the main function
if __name__ == "__main__":
    main()
