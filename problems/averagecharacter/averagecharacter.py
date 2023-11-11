i = input()

s = 0
for c in i:
    s += ord(c)

print(chr(s // len(i)))