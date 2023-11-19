from collections import Counter
print(max(0,sum([1 for v in Counter(input()).values() if v%2])-1))