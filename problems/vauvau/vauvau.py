a, b, c, d = map(int, input().split())
p, m, h = map(int, input().split())

def dog_status(t):
    x = (1 if t % (a + b) < a else 0) + (1 if t % (c + d) < c else 0)
    if x == 2:
        return "both"
    elif x == 1:
        return "one"
    else:
        return "none"

print(dog_status(p-1))
print(dog_status(m-1))
print(dog_status(h-1))