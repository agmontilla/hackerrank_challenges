def count_substring(string: str, sub_string: str) -> int:
    sub_s_dim = len(sub_string)
    count = len([True for posi in range(len(string)) if string[posi:posi+sub_s_dim] == sub_string])
    return count


def main() -> None:
    string = input()
    sub_string = input()
    print(count_substring(string, sub_string))


if __name__ == "__main__":
    main()
