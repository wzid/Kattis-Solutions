n = int(input())

m = n+1

while True:
    if sorted(str(n)) == sorted(str(m)):
        print(m)
        break
    elif len(str(m)) > len(str(n)):
        print(0)
        break
    m += 1