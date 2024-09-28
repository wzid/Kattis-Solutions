x = lambda:range(int(input()))
for i in x():
  print(len(set([input() for _ in x()])))