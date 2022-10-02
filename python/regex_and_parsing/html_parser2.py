from html.parser import HTMLParser

# create a subclass and override the handler methods


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        print(">>> {}-line Comment".format("Multi" if data.count('\n') > 0 else "Single"))
        for line in data.splitlines():
            print(f"{line}")

    def handle_data(self, data: str) -> None:
        if data != '\n':
            print(f">>> Data\n{data}")


class Reader():
    MAX_LINES = 100

    def readlines(self) -> list[str]:
        number_of_lines = int(input())
        if number_of_lines > self.MAX_LINES:
            raise ValueError("Number of lines is too big")
        lines = []
        for _ in range(number_of_lines):
            lines.append(input()+"\n")
        return lines


# instantiate the parser and fed it some HTML


def main() -> None:
    reader = Reader()
    html_content = reader.readlines()
    parser = MyHTMLParser()
    parser.feed("".join(html_content))


if __name__ == "__main__":
    main()
