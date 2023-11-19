def ordinal(n):
    if n == 0:
        return '{}'
    return '{' + ','.join(ordinal(i) for i in range(n)) + '}'

n = int(input())
print(ordinal(n))