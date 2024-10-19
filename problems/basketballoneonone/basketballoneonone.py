x = input()

a = 0
b = 0
win_by_two = False
for i in range(0, len(x), 2):
    team, score = x[i:i+2]
    score = int(score)
    
    if team == 'A':
        a += score
    else:
        b += score

print('A' if a > b else 'B')