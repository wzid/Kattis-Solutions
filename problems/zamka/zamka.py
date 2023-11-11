L = int(input())
D = int(input())
X = int(input())

def sum_of_digits(j: int) -> int:
    return sum([int(c) for c in str(j)])
    
while sum_of_digits(L) != X:
    L+= 1

while sum_of_digits(D) != X:
    D-= 1

print(L)
print(D)