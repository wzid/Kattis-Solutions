n = int(input())

l = [int(x) for x in input().split() if x != '-1']

print(sum(l) / len(l))