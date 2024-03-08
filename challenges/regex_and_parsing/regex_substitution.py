""" Regex Substitution Challenge """
import re


class RegexSubstitution:
    """Replace class"""

    PATTERN = re.compile(r"(?<= )(&&|\|\|)(?= )")

    def __init__(self, text: list[str]):
        self.text = text

    def replace(self) -> list[str]:
        """Replace && and || with and and or

        It will replace only if the && and || have a space on both sides
        """
        results: list[str] = []
        for line in self.text:
            results.append(re.sub(self.PATTERN, self._replace, line))

        return results

    def _replace(self, match: re.Match) -> str:
        """Substitute && and || with and and or"""
        target = match.group(0)
        replacements = {"&&": "and", "||": "or"}
        return replacements[target]


def main() -> None:
    """Main function"""
    rows = int(input())
    text = [input() for _ in range(rows)]

    results = RegexSubstitution(text).replace()

    print(*results, sep="\n")


if __name__ == "__main__":
    main()
