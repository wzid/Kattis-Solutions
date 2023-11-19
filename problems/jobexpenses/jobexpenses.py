input()
l = [-int(x) for x in input().split() if int(x) < 0]

print(sum(l))