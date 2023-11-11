from math import ceil

b, k, g = map(int, input().split())

groups = k // g


print(ceil((b-1) / groups))