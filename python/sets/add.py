# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    countries_number = int(input(''))
    countries = {input('') for _ in range(countries_number)}
    print(countries.__len__())
