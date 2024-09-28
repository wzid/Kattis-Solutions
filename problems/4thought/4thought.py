t = int(input())
operations = ['*', '-', '+', '//']
for i in range(t):
    n = int(input())
    found = False
    for op in operations:
        for op2 in operations:
            for op3 in operations:
                if eval(f'4 {op} 4 {op2} 4 {op3} 4') == n:
                    v = f'4 {op} 4 {op2} 4 {op3} 4 = {n}'.replace('//', '/')
                    print(v)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        print('no solution')