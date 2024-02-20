# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Mutations """

if __name__ == "__main__":

    _ = int(input())
    set_A = set(map(int, input().split()))
    total_operations = int(input())

    for _1 in range(total_operations):
        func, _2 = input().split()
        set_tmp = set(map(int, input().split()))

        getattr(set_A, func)(set_tmp)

    print(f'{sum(set_A)}')
