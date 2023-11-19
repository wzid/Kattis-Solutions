n, dm = map(int, input().split())
days = list(map(int,input().split()))

for k, i in enumerate(days):
  if i <= dm:
    print(f'It hadn\'t snowed this early in {k} years!')
    exit()
print("It had never snowed this early!")