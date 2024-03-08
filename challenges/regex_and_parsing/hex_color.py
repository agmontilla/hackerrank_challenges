""" Hex Color Challenge """
import re
from typing import Generator


class Text:
    """Text class"""

    PATTERN = re.compile(r"(?<=[: ])(#[\da-f]{3}|#[\da-f]{6})\b", flags=re.IGNORECASE)

    def __init__(self, text_lines: list[str]):
        self.text_lines = text_lines

    def get_hex_codes(self) -> Generator[str, None, None]:
        """Get hex codes in the text"""
        for sentence in self.text_lines:
            match = re.findall(self.PATTERN, sentence)
            if match:
                yield from match


def main() -> None:
    """Main function"""
    rows = int(input())
    text_lines = [input() for _ in range(rows)]

    text = Text(text_lines)
    print("\n".join(text.get_hex_codes()))


if __name__ == "__main__":
    main()
