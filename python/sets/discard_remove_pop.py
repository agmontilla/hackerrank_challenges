""" Discard, Remove, Pop """

if __name__ == "__main__":

    n = int(input())
    s = set(map(int, input().split()))
    operations_number = int(input())

    while operations_number > 0:
        func, *args = input().split()
        getattr(s, func)(*map(int, args))
        operations_number -= 1

    print(f'{sum(s)}')
