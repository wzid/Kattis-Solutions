c = int(input())

for i in range(c):
    l = list(map(int, input().split()))
    n = l.pop(0)
    avg = sum(l) / n
    l = list(filter(lambda x: x > avg, l))
    v = (len(l) / n) * 100
    print(f'{v:.3f}%')

