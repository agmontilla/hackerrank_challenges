"""" Validating and Parsing Email Addresses Challenge """
import re
from email.utils import formataddr, parseaddr
from typing import Generator


class Users:
    """Users class"""

    PATTERN = re.compile(r"^([a-zA-Z])([A-Za-z0-9_.\-]{1,})@([a-zA-Z]{1,})\.([a-zA-Z]{1,3})$")

    def __init__(self, users: list[tuple[str, str]]):
        self.users = users

    def get_valid_email_addresses(self) -> Generator[str, None, None]:
        """Get valid email addresses"""
        for user, email in self.users:
            if re.search(self.PATTERN, email):
                yield formataddr((user, email))


def main() -> None:
    """Main function"""
    n = int(input())
    rows = [parseaddr(input()) for _ in range(n)]

    users = Users(rows)
    print("\n".join(users.get_valid_email_addresses()))


if __name__ == "__main__":
    main()
