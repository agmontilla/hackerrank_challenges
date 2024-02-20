# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Check Strict Superset """

if __name__ == "__main__":

    set_a = set(input().split())

    checks = [set_a.issuperset(set(input().split()))
              for _ in range(int(input()))]

    print(all(checks))
