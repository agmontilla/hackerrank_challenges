# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    test_cases = int(input())

    sets = [(int(input()), set(input().split()))
            for _ in range(test_cases) for _ in range(2)]

    for i in range(0, 2*test_cases, 2):
        print(sets[i][1].issubset(sets[i+1][1]))
