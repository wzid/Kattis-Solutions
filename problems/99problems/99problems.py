i = int(input())

l = i
r = i

while True:
    l+=1
    r-=1
    if str(l)[::-1][:2] == '99':
        print(l)
        break
    elif str(r)[::-1][:2] == '99':
        print(r)
        break