""" Validating UID Challenge """
import re
from typing import Generator


class UUIDCollection:
    """UUID Collection class"""

    UPPER_CASE = r"(?=(?:.*[A-Z]){2,})"
    DIGITS = r"(?=(?:.*\d){3,})"
    ONLY_ALPHANUMERIC = r"[a-zA-Z0-9]{10}"
    REPEATED_CHARACTERS = r"(?!.*(.).*\1)"

    VALIDATORS = (UPPER_CASE, DIGITS, ONLY_ALPHANUMERIC, REPEATED_CHARACTERS)

    def __init__(self, uuids: list[str]):
        self.uuids = uuids

    def are_valid(self) -> Generator[str, None, None]:
        """Check if the UUIDs are valid
        Returns a generator with the result of the validation
        The possible results are "Valid" or "Invalid" for every UUID
        """
        for uuid in self.uuids:
            match = [re.match(validator, uuid) for validator in self.VALIDATORS]
            yield ("Valid" if all(match) else "Invalid")


def main() -> None:
    """Main function"""
    test_cases = int(input())
    uuids = [input() for _ in range(test_cases)]

    print(*list(UUIDCollection(uuids).are_valid()), sep="\n")


if __name__ == "__main__":
    main()
