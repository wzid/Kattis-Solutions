testcases = int(input())

for i in range(testcases):
    n = int(input())
    cities = set()
    for j in range(n):
        cities.add(input())
    print(len(cities))
        