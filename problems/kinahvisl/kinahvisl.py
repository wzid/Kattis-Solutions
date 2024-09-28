# n, x = map(int, input().split())
x = input()
y = input()
co = 0
for i in range(len(x)):
    if x[i] != y[i]:
        co += 1
print(co+1)