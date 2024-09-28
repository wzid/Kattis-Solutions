n = int(input())
got = set()
for i in range(n):
    x = input()
    got.add(x)
    #print(f'Takk {x}')

if len(got) == 2:
    print('blandad best')
else:
    print(got.pop())