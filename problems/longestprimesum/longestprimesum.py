n = int(input())

s = 0
if n % 2: 
    s += 1
    n -= 3
    

s += n // 2

print(s)