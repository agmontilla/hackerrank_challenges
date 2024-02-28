""" Named Tuple Chhallenge """
from typing import NamedTuple


class Student(NamedTuple):
    """Student class"""

    id_: str
    marks_: str
    name_: str
    class_: str


def transform_signature_fields(fields: list[str]) -> list[str]:
    """Process fields
    - Add an underscore to each field
    - Convert each field to lowercase
    """
    return [field + "_" for field in (map(str.lower, fields))]


def process_inputs(fields: list[str], students: list) -> list[Student]:
    """Process inputs"""
    return [Student(**dict(zip(fields, student.split()))) for student in students]


def get_average_mark(students: list[Student]) -> float:
    """Get the average mark of the students"""
    return sum(int(student.marks_) for student in students) * 1.00 / len(students)


def main() -> None:
    """Main function"""
    regs = int(input())
    fields = transform_signature_fields(input().split())

    students = process_inputs(fields, [input() for _ in range(regs)])

    print(f"{get_average_mark(students):.2f}")


if __name__ == "__main__":
    main()
