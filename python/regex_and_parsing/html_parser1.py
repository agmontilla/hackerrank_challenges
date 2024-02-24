""" HTML Parser - Part 1 """
# pylint: disable=duplicate-code

from abc import ABC
from html.parser import HTMLParser
from typing import List, Optional, Tuple

from .utils import Reader

# create a subclass and override the handler methods


class MyHTMLParser(HTMLParser, ABC):
    """MyHTMLParser"""

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        print(f"Start : {tag}")
        self._print_attrs(attrs)

    def handle_endtag(self, tag: str) -> None:
        print(f"End   : {tag}")

    def handle_startendtag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        print(f"Empty : {tag}")
        self._print_attrs(attrs)

    def _print_attrs(self, attrs: List[Tuple[str, Optional[str]]]) -> None:
        for attr_name, attr_value in attrs:
            print(f"-> {attr_name} > {attr_value if attr_value else 'None'}")


def main() -> None:
    """Main function"""
    reader = Reader()
    html_content = reader.readlines()
    parser = MyHTMLParser()
    parser.feed("".join(html_content))


if __name__ == "__main__":
    main()
