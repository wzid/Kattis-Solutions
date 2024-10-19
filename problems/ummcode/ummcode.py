words = input().split()

otherchars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstvwxyz'

letter = 0x00
index = 6
real_word = ''
for word in words:
    is_umm = True
    for c in word:
        if c in otherchars:
            is_umm = False
            break
    
    if is_umm:
        for c in word:
            if c == 'u':
                x = 1 << index
                letter |= x
            if c == 'u' or c == 'm':
                index -= 1
            if index < 0:
                real_word += chr(letter)
                index = 6
                letter = 0x00
print(real_word)