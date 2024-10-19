n, k = map(int, input().split())


times = []

for i in range(n):
    enter_time, exit_time = map(int, input().split())    
    times.append((enter_time, 0))
    times.append((exit_time, 1))

# at i: current_people + the number of people the enter for the next k ms

times.sort()

current_people = 0
m = 0
right = 0
rolling_count = 0
for time in times:
    start = time[0]
    while right < len(times) and times[right][0] - start <= k:
        if times[right][1] == 0:
            rolling_count += 1
        right += 1
    
    m = max(m, rolling_count)
    
    if time[1] == 1:
        rolling_count -= 1

print(m)