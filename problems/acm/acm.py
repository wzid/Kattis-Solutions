solved = set()
from collections import defaultdict
prev_wrong = defaultdict(int)
total_score = 0

while (x := input()) != '-1':
    m, letter, correct = x.split()
    m = int(m)
    correct = correct == 'right'
    
    if correct and letter not in solved:
        total_score += m + prev_wrong[letter] * 20
        solved.add(letter)
    elif not correct:
        prev_wrong[letter] += 1


print(len(solved), total_score)