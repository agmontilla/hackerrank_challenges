from typing import List
from html.parser import HTMLParser
from typing import Optional, Tuple

# create a subclass and override the handler methods


class MyHTMLParser(HTMLParser):
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


class Reader():
    MAX_LINES = 100

    def readlines(self) -> List[str]:
        number_of_lines = int(input())
        if number_of_lines > self.MAX_LINES:
            raise ValueError("Number of lines is too big")
        lines = []
        for _ in range(number_of_lines):
            lines.append(input())
        return lines


# instantiate the parser and fed it some HTML


def main() -> None:
    reader = Reader()
    html_content = reader.readlines()
    parser = MyHTMLParser()
    parser.feed("".join(html_content))


if __name__ == "__main__":
    main()
