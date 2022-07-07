def swap_case(s: str) -> str:
    characters = [ch.lower() if ch.isupper() else ch.upper() for ch in s]
    return ''.join(characters)


def main() -> None:
    sample = "HackerRank.com presents \"Pythonist 2\"."
    print(swap_case(sample))


if __name__ == "__main__":
    main()
