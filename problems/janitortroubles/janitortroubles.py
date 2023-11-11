import math
a , b ,c , d = map(int , input().split())
s = 0.5*(a + b + c +d)
a = (s-a)*(s-b)*(s-c)*(s-d)
print(math.sqrt(a))