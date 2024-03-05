""" Zipped! Challenge """


def get_average_score(subjects: list[list[float]]) -> list[float]:
    """Get the average score of each student"""
    return [sum(student) / len(student) for student in zip(*subjects)]


def main() -> None:
    """Main function"""
    n, x = input().split()
    subjects = []

    for _ in range(int(x)):
        subjects.append(list(map(float, input().split()))[: int(n)])

    results = get_average_score(subjects)

    print(*results, sep="\n")


if __name__ == "__main__":
    main()
