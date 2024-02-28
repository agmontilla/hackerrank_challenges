""" Named Tuple Chhallenge

This was my simply solution to this:

Old solution:
```python
from collections import namedtuple

if __name__ == "__main__":
    regs, Student = int(input()), namedtuple('Student', input().split())
    students = [Student(*input().split()) for _ in range(regs)]
    print(sum([int(person.MARKS) for person in students])*1.00 / len(students))
```

But when I wanted to write unit test for this, I had some issues.
I had to refactor the code to make it testable.
"""
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
