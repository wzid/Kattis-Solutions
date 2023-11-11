m = input()

underscore = 0
lowercase = 0
uppercase = 0
symbol = 0

for c in m:
    if c == '_':
        underscore += 1
    elif c.isalpha():
        if c.islower():
            lowercase += 1
        else:
            uppercase += 1
    else:
        symbol += 1


print(underscore / len(m))
print(lowercase / len(m))
print(uppercase / len(m))
print(symbol / len(m))
