b, br, bs, a, As = map(int, input().split())

total = 0

while total <= abs(br - b) * bs:
  total += As
  a += 1

print(a)