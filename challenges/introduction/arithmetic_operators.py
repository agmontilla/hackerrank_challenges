""" Arithmetic Operators """


def show_arithmetic_operations(a: int, b: int) -> None:
    """Show arithmetic operations"""
    print(f"{a + b}")
    print(f"{a - b}")
    print(f"{a * b}")


def main() -> None:
    """Main function"""
    show_arithmetic_operations(int(input()), int(input()))


if __name__ == "__main__":
    main()
