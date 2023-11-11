import math
t = int(input())

for i in range(1, t+1):
    a = math.factorial(int(input()))
    print(int(str(a)[-1]))