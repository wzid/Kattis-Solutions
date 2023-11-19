import sys

words = []
for line in sys.stdin:
    line = line.rstrip()
    line = line.split()
    words.append(line[0])
    if len(line) > 1:
        words.append(line[1])

permutations = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i == j:
            continue
        permutations.add(words[i] + words[j])
permutations = list(permutations)
permutations.sort()

for word in permutations:
    print(word)