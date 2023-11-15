l = list(map(int, input().split()))
n, kwf = map(int, input().split())

k =0 
for i in range(5):
    k += l[i*2]* l[i*2+1]
print(n*(k//5)//kwf)