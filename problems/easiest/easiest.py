
def sum_digits(x):
  return sum(map(int, list(str(x))))

while True:
  n = int(input())
  if n == 0:
    exit()

  sum_dig = sum_digits(n)
  pr = 11
  while True:
    if sum_dig == sum_digits(pr *n):
      print(pr)
      break
    pr += 1