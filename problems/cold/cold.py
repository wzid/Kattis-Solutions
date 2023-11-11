n = int(input())

l = list(map(int, input().split()))


s = 0

for element in l:
    if element < 0:
        s += 1

print(s)