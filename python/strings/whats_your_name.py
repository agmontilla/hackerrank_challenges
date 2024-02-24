""" What's Your Name? """


def print_full_name(a: str, b: str) -> None:
    """Print the full name"""
    print(f"Hello {a} {b}! You just delved into python.")


def main() -> None:
    """Main function"""
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


if __name__ == "__main__":
    main()
