""" Find the maximum depth of an XML tree Challenge
I don't want to use the global statement, but the challenge requires it.
"""
import xml.etree.ElementTree as etree

MAXDEPTH = 0


def depth(elem: etree.Element, level: int) -> int:
    """Find the maximum depth of an XML tree"""
    global MAXDEPTH  # pylint: disable=global-statement
    level += 1

    MAXDEPTH = max(MAXDEPTH, level)

    for child in elem:
        depth(child, level)

    return MAXDEPTH


def main() -> None:
    """Main function"""
    n = int(input())
    xml = ""
    for _ in range(n):
        xml = xml + input() + "\n"

    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(MAXDEPTH)


if __name__ == "__main__":
    main()
