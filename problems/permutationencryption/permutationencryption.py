import math
while ((x := input()) != '0'):
    x = x.split()
    n = int(x[0])
    perm = list(map(int, x[1:]))
    msg = [c for c in input()]

    spaces_needed = (math.ceil(len(msg) / n) * n) - len(msg)
    for i in range(spaces_needed):
        msg.append(' ')


    for i in range(0, len(msg), len(perm)):
        tmp = ''
        for v in perm:
            tmp += msg[i+v-1]
        
        for j, c in enumerate(tmp):
            msg[i+j] = c
    
    msg ='\'' + ''.join(msg) + '\''
    print(msg)