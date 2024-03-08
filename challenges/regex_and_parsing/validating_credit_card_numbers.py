""" Validating Credit Card Numbers Challenge """

import re
from typing import Generator


class CreditCardNumberCollection:
    """A class to validate credit card numbers"""

    MINIMAL_CONDITIONS = r"^[456]{1}[0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}$"
    REPEATED_CHARACTERS = r"(\d)\1{3}"

    def __init__(self, credit_cards: list[str]):
        self.credit_cards = credit_cards

    def _meet_minimum_conditions(self, credit_card: str) -> bool:
        """Check if the credit card number meets the minimum conditions
        1. It must start with 4, 5, or 6
        2. It must contain exactly 16 digits
        3. It must only consist of digits (0-9)
        4. It may have digits in groups of 4, separated by one hyphen "-"
        5. It must NOT use any other separator like ' ' , '_', etc.
        """
        return re.match(self.MINIMAL_CONDITIONS, credit_card) is not None

    def _has_repeated_characters(self, credit_card: str) -> bool:
        """Check if the credit card number has repeated characters

        It must NOT have 4 or more consecutive repeated digits
        """
        return re.search(self.REPEATED_CHARACTERS, credit_card.replace("-", "")) is not None

    def are_valid(self) -> Generator[str, None, None]:
        """Check if the credit card numbers are valid or not"""
        for credit_card in self.credit_cards:
            if self._meet_minimum_conditions(credit_card) and not self._has_repeated_characters(credit_card):
                yield "Valid"
            else:
                yield "Invalid"


def main() -> None:
    """Main function"""
    rows = int(input())
    credit_cards = [input() for _ in range(rows)]

    print(*list(CreditCardNumberCollection(credit_cards).are_valid()), sep="\n")


if __name__ == "__main__":
    main()
