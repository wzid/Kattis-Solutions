n = int(input())
first = 0
second = 0
third = 0
for i in range(n):
    l = list(map(str, input().split()))
    first += 1 if l[0] == 'J' else 0
    second += 1 if l[1] == 'J' else 0
    third += 1 if l[2] == 'J' else 0

print(min(first, second,third))
    