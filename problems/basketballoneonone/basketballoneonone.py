s = input()

score = [0, 0]
ten = False
for i in range(1, len(s), 2):
    if s[i-1] ==  'A':
        score[0] += int(s[i])
    elif s[i - 1] == 'B':
        score[1] += int(s[i])

    if score[0] == 10 and score[1] == 10:
        ten = True
    elif not ten:
        if score[0] >= 11:
            break
        elif score[1] >= 11:
            break
    elif ten:
        if score[0] - 2 == score[1]:
            break
        elif score[1] - 2 == score[0]:
            break

if not ten:
    if score[0] >= 11:
        print('A')
    elif score[1] >= 11:
        print('B')
elif ten:
    if (score[0] - 2) >= score[1]:
        print('A')
    elif (score[1] - 2) >= score[0]:
        print('B')
