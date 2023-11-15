n, pred, s = map(int, input().split())

for i in range(s):
  m = list(map(int, input().split()))[1:]
  if pred in m:
    print("KEEP")
  else:
    print("REMOVE")