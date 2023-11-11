ciphertext = input()
key = input()
m = ''
for i in range(len(ciphertext)):
    c = ord(ciphertext[i]) - 65
    k = ord(key[i]) - 65
    if i % 2 == 0:
        a = (c - k) % 26
    else:
        a = (c + k) % 26
    a = chr(a+65)
    m += a

print(m)