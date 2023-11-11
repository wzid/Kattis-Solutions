
n = int(input())
s = input()
size = 1
index = 0
found = False
for i in range(1, n):
    if i == 10:
        size = 2
    elif i == 100:
        size = 3
    
    num = int(s[index:index+size])
    if i != num:
        print(i)
        found = True
        break
    index += size

if not found:
    print(i+1)