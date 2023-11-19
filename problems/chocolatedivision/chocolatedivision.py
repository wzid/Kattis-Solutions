a, b = map(int, input().split())

cuts = a*b
cuts -=1
if cuts %2==0:
    print('Beata')
else:
    print('Alf')