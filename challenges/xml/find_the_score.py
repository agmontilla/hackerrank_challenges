""" XML 1 - Find the Score Challenge """

import sys
import xml.etree.ElementTree as etree


def get_attr_number(root: etree.Element) -> int:
    """Get the number of attributes in the XML tree"""
    attr_count = len(root.attrib) + sum(get_attr_number(child) for child in root)
    return attr_count


def main() -> None:
    """Main function"""
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


if __name__ == "__main__":
    main()
