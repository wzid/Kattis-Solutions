n = int(input())
while n != 0:
    first = []
    
    for i in range(n):
        first.append(int(input()))
    
    second = []
    for i in range(n):
        second.append(int(input()))
    first_sorted = sorted(first)
    second.sort()
    for p in first:
        print(second[first_sorted.index(p)])
    print()
    n = int(input())