import sys

words = set()
for line in sys.stdin:
    line = line.strip()
    result = []
    for word in line.split():
        if word.lower() in words:
            result.append('.')
        else:
            result.append(word)
            words.add(word.lower())
    print(' '.join(result))