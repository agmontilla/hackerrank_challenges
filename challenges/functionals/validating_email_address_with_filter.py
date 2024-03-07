""" Validating Email Address with a Filter Challenge """
import re

PATTERN = re.compile("(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[.][a-zA-Z]{1,3})$")


def fun(s: str) -> bool:
    """Returns True if the email is valid, False otherwise."""
    return PATTERN.search(s) is not None


def filter_mail(emails: list[str]) -> list[str]:
    """Filters the emails based on the fun function."""
    return list(filter(fun, emails))


def main() -> None:
    """Main function."""
    n = int(input())
    emails = [input() for _ in range(n)]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)


if __name__ == "__main__":
    main()
