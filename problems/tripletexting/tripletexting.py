from collections import defaultdict
d = defaultdict(int)
s = input()

skip = len(s) // 3

for i in range(3):
    d[s[i*skip:(skip*(i+1))]] += 1


print(max(d, key=d.get))