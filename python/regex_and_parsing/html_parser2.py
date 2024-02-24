""" HTML Parser - Part 2 """
# pylint: disable=duplicate-code

from abc import ABC
from html.parser import HTMLParser

from .utils import Reader

# create a subclass and override the handler methods


class MyHTMLParser(HTMLParser, ABC):
    """MyHTMLParser"""

    def handle_comment(self, data: str) -> None:
        print(">>> {}-line Comment".format("Multi" if data.count("\n") > 0 else "Single"))
        for line in data.splitlines():
            print(f"{line}")

    def handle_data(self, data: str) -> None:
        if data != "\n":
            print(f">>> Data\n{data}")


def main() -> None:
    """Main function"""
    reader = Reader()
    html_content = reader.readlines()
    parser = MyHTMLParser()
    parser.feed("".join(html_content))


if __name__ == "__main__":
    main()
