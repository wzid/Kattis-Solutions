n = int(input())

word = []

for i in range(n):
  word.append(input())

if word == sorted(word):
  print("INCREASING")
elif word == sorted(word, reverse=True):
  print("DECREASING")
else:
  print('NEITHER')