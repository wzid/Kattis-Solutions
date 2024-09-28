area = .5

width = 2**(-5/4)
height = 2**(-3/4)

n = int(input()) - 1
l = list(map(int, input().split()))

# attempt 2
tape = 0
a = 2
resolved = False
for i, item in enumerate(l):
    tape += 2**((-3-i*2)/4) * a / 2
    a -= item
    a *= 2
    if a <= 0:
        resolved = True
        break
if resolved:
    print(tape)
else:
    print("impossible")
