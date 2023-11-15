from math import ceil
s, t, n = map(int, input().split())

walk_times = list(map(int, input().split()))

ride_time = list(map(int, input().split()))

interval_times_bus = list(map(int, input().split()))

for i in range(n):
    s += walk_times[i]
    s = ceil(s / interval_times_bus[i]) * interval_times_bus[i]
    s += ride_time[i]

s += walk_times[-1]

if s <= t:
    print('yes')
    
else:
    print('no')