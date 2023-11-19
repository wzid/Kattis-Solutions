r, n = map(int, input().split())

rooms = [int(input()) for i in range(n)]

for i in range(1, r + 1):
  if i not in rooms:
    print(i)
    exit()
print('too late')