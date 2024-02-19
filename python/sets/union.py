# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Set .union() Operation """

if __name__ == "__main__":

    n1 = int(input())
    english_students = set(map(int, input().split()))
    n2 = int(input())
    french_students = set(map(int, input().split()))

    students_total = len(english_students.union(french_students))

    print(f'{students_total}')
