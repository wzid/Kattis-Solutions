def length(n: int) -> int:
    if n <= 2:
        return n
    if n == 3:
        return 4
    return length(n-1) + length(n-2) + length(n-3)
    
print(length(int(input())))