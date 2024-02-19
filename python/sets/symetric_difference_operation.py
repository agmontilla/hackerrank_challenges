# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Set .symmetric_difference() Operation """
# pylint: disable=duplicate-code

if __name__ == "__main__":

    _ = int(input())
    english_students = set(map(int, input().split()))
    _ = int(input())
    french_students = set(map(int, input().split()))

    students_total = len(
        english_students.symmetric_difference(french_students))

    print(f'{students_total}')
