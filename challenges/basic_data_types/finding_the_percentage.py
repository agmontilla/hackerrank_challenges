""" Finding the percentage """


def percentage(student_marks: dict, query_name: str) -> str:
    """Given a dictionary of students and their scores, calculate the average
    of the scores of the student whose name is given.
    """
    average: float = 0

    if query_name in student_marks:
        average = sum(student_marks[query_name]) / len(student_marks[query_name])

    return f"{average:.2f}"


def main() -> None:
    """Main function."""
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(percentage(student_marks, query_name))


if __name__ == "__main__":
    main()
