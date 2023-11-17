import math

current, target, n = (int(s) for s in input().split(' '))
blades = []
for o in range(n):
    ma, t = (int(s) for s in input().split(' '))
    blades.append([ma, t])
blades.sort(reverse=True)

# we can't keep blades of the same size with different speeds. we must discard all blades that are not the lowest speed

# remove blades that just get progressively weaker

filtered_blades= []
filtered_blades.append(blades[0])
for i in range(1, n):
    m, h = blades[i]
    if h < filtered_blades[-1][1]:
        while m == filtered_blades[-1][0]:
            filtered_blades.pop()
        filtered_blades.append((m, h))

blades = filtered_blades

n = len(blades)

# check for no suittable blade
five = math.log(.5)
if blades[0][0] < current:
    print(-1)
else:
    s = 0
    ind = 0
    for a in range(1, n):
        from_size = max(target, min(blades[ind][0], current))
        to_size = max(target, min(blades[a][0], current))

        s += blades[ind][1] * ((math.log(to_size/from_size))/five)
        ind = a

    times = min(max(blades[ind][0], target), current)
    s += blades[ind][1] * ((math.log(target/times))/five)


    print(s)