n = int(input())

for i in range(n):
    s = input().lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    works = []
    for c in alpha:
        if c not in s:
            works.append(c)
            
    if not works:
        print('pangram')
    else:
        f =''.join(works)
        print(f'missing {f}')