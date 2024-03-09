"""" Validating Postal Codes Challenge

Hackerrank solution:
```python
import re
regex_integer_in_range = r"\b[0-9]{6}\b"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\\d)(?=\\d\1)"  # Do not delete 'r'.
P = input()
print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

But this time I want to use Protocol feature to define the Checkeable class.

A protocol is a class that defines a set of methods; a class can be said to implement a protocol
if it has an instance of the protocol as a parent class, or if it has all the methods defined in the protocol.
```
"""
import re
from typing import Protocol


class Checkeable(Protocol):
    """Checkeable class"""

    def check(self, postal_code: str) -> bool:
        """Returns True if the postal code is valid given a condition, otherwise False."""


class IsInRange:
    """Returns True if the postal code is in range, otherwise False.
    Range is defined as 100000 <= postal_code <= 999999
    """

    INTEGER_IN_RANGE = r"\b[0-9]{6}\b"

    def check(self, postal_code: str) -> bool:
        """Returns True if the postal code is in range, otherwise False.
        Range is defined as 100000 <= postal_code <= 999999
        """
        return bool(re.match(self.INTEGER_IN_RANGE, postal_code))


class HasAlternatingRepetitiveDigitPair:
    """Returns True if the postal code has alternating repetitive digit pair, otherwise False.
    Alternating repetitive digit pair is defined as 123123 or 1212"""

    ALTERNATING_REPETITIVE_DIGIT_PAIR = r"(\d)(?=\d\1)"

    def check(self, postal_code: str) -> bool:
        """Returns True if the postal code has alternating repetitive digit pair, otherwise False.
        Alternating repetitive digit pair is defined as 123123 or 1212
        """
        return len(re.findall(self.ALTERNATING_REPETITIVE_DIGIT_PAIR, postal_code)) < 2


class PostalCode:
    """Postal Code class"""

    def __init__(self, postal_code: str, validations: list[Checkeable]) -> None:
        self.postal_code = postal_code
        self.validations = validations

    def is_valid(self) -> bool:
        """Returns True if the postal code is valid, otherwise False."""
        return all(validation.check(self.postal_code) for validation in self.validations)


def main() -> None:
    """Main function"""
    postal_code = PostalCode(
        input(),
        validations=[IsInRange(), HasAlternatingRepetitiveDigitPair()],
    )
    print(postal_code.is_valid())


if __name__ == "__main__":
    main()
