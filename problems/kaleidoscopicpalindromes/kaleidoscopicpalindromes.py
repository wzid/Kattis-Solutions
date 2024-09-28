a, b, k = map(int, input().split())
CHAR_FOR_INT = '0123456789abcdef'

def to_string(n, base):
    if n < base:
        return CHAR_FOR_INT[n]

    return to_string(n // base, base) + CHAR_FOR_INT[n % base]

count = 0
# inclusive range
for num in range(a, b+1):
    isPalindrome = True
    for j in range(2, k+1):
        x = to_string(num, j)
        if x != x[::-1]:
            isPalindrome = False
            break
    if isPalindrome:
        count += 1

print(count)

