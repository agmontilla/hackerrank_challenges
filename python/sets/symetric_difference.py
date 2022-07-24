# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    sets = []

    for _ in range(2):
        n = int(input())
        sets.append(list(map(int, input().split()))[:n])

    unique = []

    for x_pos, x in enumerate(sets):
        for y_pos, y in enumerate(sets):
            if x_pos != y_pos:
                unique.extend(list(set(x).difference(set(y))))

    print(*sorted(unique), sep='\n')
