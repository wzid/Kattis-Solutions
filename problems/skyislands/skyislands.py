n, m = map(int, input().split())

if m < n - 1: # some theorem
  print("NO")
  quit()

if m == 0:
  if n == 1:
    print('YES')
  else:
    print('NO')
  quit()

colors = list(range(n))


for i in range(m):
  a, b = map(int, input().split())

  colorA = colors[a-1]
  colorB = colors[b-1]
  # Replace 
  for j in range(n):
    if colors[j] == colorA:
      colors[j] = colorB

firstColor = colors[0]
for color in colors:
  if color != firstColor:
    print("NO")
    quit()
print('YES')