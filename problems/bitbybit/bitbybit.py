n = int(input())

while n != 0:
    s = list('?'*32)
    for i in range(n):
        x = input().split()
        action = x[0]

        if action == 'SET':
            s[int(x[1])] = '1'
        elif action == 'CLEAR':
            s[int(x[1])] = '0'
        elif action == 'AND':
            val1, val2 = int(x[1]), int(x[2])

            if s[val1] == '1' and s[val2] == '1':
                s[val1] = '1'
            elif s[val1] == '0' or s[val2] == '0':
                s[val1] = '0'
            else:
                s[val1] = '?'
        elif action == 'OR':
            val1, val2 = int(x[1]), int(x[2])

            if s[val1] == '1' or s[val2] == '1':
                s[val1] = '1'
            elif s[val1] == '0' and s[val2] == '0':
                s[val1] = '0'
            else:
                s[val1] = '?'

            
    # 111
    print(''.join(s[::-1]))

    n = int(input())