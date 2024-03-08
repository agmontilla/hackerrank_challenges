""" Validating phone number challenge """
import re


class PhoneNumbers:
    """Phone numbers class"""

    PATTERN = re.compile(r"^(7|8|9)(\d{9})$")

    def __init__(self, phone_numbers: list[str]):
        self.phone_numbers = phone_numbers

    def are_valid(self) -> list[str]:
        """Check if phone numbers are valid

        Returns a list of strings with "YES" or "NO" for each phone number
        """
        results = []
        for phone_number in self.phone_numbers:
            results.append("YES" if re.search(self.PATTERN, phone_number) else "NO")

        return results


def main() -> None:
    """Main function"""
    n = int(input())
    phone_numbers = [input() for _ in range(n)]
    results = PhoneNumbers(phone_numbers).are_valid()

    print(*results, sep="\n")


if __name__ == "__main__":
    main()
