from collections import defaultdict
l, k, s = map(int, input().split())

finish = []
count = defaultdict(int)
time = defaultdict(int)

for i in range(l):
    x = input().split()
    bib_no, lap_time = int(x[0]), x[1]

    split_lap = lap_time.split('.')
    time[bib_no] += int(split_lap[0]) * 60 + int(split_lap[1])
    count[bib_no] += 1
    
    if count[bib_no] == k:
        finish.append((time[bib_no], bib_no))


finish.sort()

for f in finish:
    print(f[1])