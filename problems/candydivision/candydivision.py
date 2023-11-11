n = int(input())

friends = []

for i in range(int(n**.5)):
    if n % (i+1) == 0:
        friends.append(i)
        v = int(n/(i+1)) - 1
        friends.append(v)

friends = list(set(friends))
friends.sort()
print(*friends)

