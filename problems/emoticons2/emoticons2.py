

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))


faces = ''':)
:-)
:-(
;-)
xD
^_^
-_-
^o^
^^;
(..)'''.split("\n")

def emojify(x):
    x = list(x)
    i = 0
    count = 0
    while i < len(x):
        for face in faces:
            fl = len(face)
            # print(x[i:i+fl])
            if x[i:i+fl] == list(face):
                i += fl - 1
                break
        count += 1
        i += 1
    # print(x)
    return count

# print(emojify("Hello ;-)"))
# quit()

symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

s = input()
shortest = 999
longest = -1
for a in symbols:
    for b in symbols:
        
        l = emojify(s.replace(a, b, -1))
        shortest = min(shortest, l)
        longest = max(longest, l)

print(shortest, longest)

