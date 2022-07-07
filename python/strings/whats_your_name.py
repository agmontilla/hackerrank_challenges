def print_full_name(a: str, b: str) -> None:
    print("Hello {} {}! You just delved into python.".format(a, b))


def main() -> None:
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


if __name__ == "__main__":
    main()
