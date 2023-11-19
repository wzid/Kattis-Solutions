n, queries = map(int, input().split())

x = list(map(int, input().split()))

for i in range(queries):
  ty, a, b = map(int, input().split())
  if ty == 1:
    x[a-1] = b
  else:
    print(abs(x[a-1]-x[b-1]))