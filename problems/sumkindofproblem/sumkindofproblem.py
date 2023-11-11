P = int(input())

for i in range(P):
    K, N = map(int, input().split())
    integers = (N*(N+1))//2
    even = N*(N+1)
    odd = N*N
    
    print(K, integers, odd, even)