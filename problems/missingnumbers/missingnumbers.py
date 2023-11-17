n = int(input())
letters = set()
for i in range(n):
  letters.add(int(input()))

ma = max(letters)
found = False
for i in range(1, ma+1):
  if i not in letters:
    found = True
    print(i)

if not found:
  print("good job")