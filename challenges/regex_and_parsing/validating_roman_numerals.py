""" Validating Roman Numerals """
import re

REGEX_PATTERN = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IV|IX|V?I{0,3})$"


def is_a_roman_number(roman_number: str) -> bool:
    """Main function"""
    return bool(re.match(REGEX_PATTERN, roman_number))


def main() -> None:
    """Main function"""
    roman_number = input()
    print(is_a_roman_number(roman_number))


if __name__ == "__main__":
    main()
