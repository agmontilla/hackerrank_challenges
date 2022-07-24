# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    _ = int(input())
    set_A = set(map(int, input().split()))
    total_operations = int(input())

    for _ in range(total_operations):
        func, _ = input().split()
        set_tmp = set(map(int, input().split()))

        getattr(set_A, func)(set_tmp)

    print(f'{sum(set_A)}')
