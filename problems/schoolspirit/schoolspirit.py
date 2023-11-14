n = int(input())


def calc_score(l) -> float:
    group_score = 0
    for i, v in enumerate(l):
        group_score += v*((4/5)**i)
    return group_score * (1/5)

l = []
group_score = 0
for i in range(n):
    v = int(input())
    group_score += v*((4/5)**i)
    l.append(v)

group_score *= 1/5

avg = 0
for i in range(len(l)):
    # we need the list without the ith element
    avg += calc_score(l[:i] + l[i+1:])

print(group_score)
print(avg / n)