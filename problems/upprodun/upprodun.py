n = int(input())
m = int(input())

size_min = m // n
size_max = size_min + 1
leftover = m % n

for i in range(n):
    output = "*" * size_min
    if i < leftover:
        output += "*"
    print(output)