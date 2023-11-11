n=int(input())
a=[int(x)for x in input().split()]
s=-1
f=0
for i in range(1,len(a)):
    if a[i]<a[i-1] and s == -1:
        s=i-1
    elif s!=-1 and a[i]>a[i-1]:
        u=a[:s]+a[s:i][::-1]+a[i:]
        if u==sorted(a):
            print('Yes')
        else:
            print('No')
        f = 1
        break

if not f:
    if s != -1:
        u=a[:s]+a[s:][::-1]
        if u == sorted(a):
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')