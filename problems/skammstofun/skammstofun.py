n = input()
words = input().split()

abrv = ''
for word in words:
    if word[0].isupper():
        abrv += word[0]
print(abrv)