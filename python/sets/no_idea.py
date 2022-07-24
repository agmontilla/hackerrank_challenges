# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    arr_dim, set_dim = map(int, input().split())
    arr = list(map(int, input().split()))[:arr_dim]
    set_A, set_B = [set(map(int, input().split()[:set_dim])) for _ in range(2)]

    happines = 0
    for elem in arr:
        if elem in set_A:
            happines += 1
        elif elem in set_B:
            happines -= 1

    print(happines)
