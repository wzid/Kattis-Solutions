n = int(input())

for i in range(n):
    s = input()
    if s == 'P=NP':
        print('skipped')
    else:
        a, b = map(int, s.split('+'))
        print(a+b)