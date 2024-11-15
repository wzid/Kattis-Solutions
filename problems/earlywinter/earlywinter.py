n, d = map(int, input().split())

l = list(map(int, input().split()))

for i, v in enumerate(l):
    if v <= d:
        print(f"It hadn't snowed this early in {i} years!")
        exit()
print("It had never snowed this early!")