def fme(base, exponent, mod) -> int:
    d = {}
    d[1] = base
    last_result = base
    current_exponent = 2
    while exponent > current_exponent:
        d[current_exponent] = last_result**2 % mod
        last_result = d[current_exponent]
        current_exponent *= 2
    current_exponent //= 2
    result = 1
    while exponent > 0:
        if exponent >= current_exponent:
            current_exponent = max(1, current_exponent)
            result *= d[current_exponent]
            result %= mod
            exponent -= current_exponent
        current_exponent //= 2

    
    return result
    
n = int(input())

for i in range(n):
    x = int(input()) 

    count = fme(9, x-1, 1000000007)
    count *= 8
    print(count % 1000000007)