x = 'abcdefghijklmnopqrstuvwxyz'
co = 0
y = input()
for c in y:
    if c.lower() in x:
        co += 1
print(co)