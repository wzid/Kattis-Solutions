import sys

for line in sys.stdin:
    line = line.split()
    end_hour = line[-1].split(':')
    start_hour = line[-2].split(':')
    hour_diff = int(end_hour[0]) - int(start_hour[0])
    start_min = int(start_hour[1])
    end_min = int(end_hour[1])
    minutes = 0
    if start_min > end_min:
        hour_diff -= 1
        minutes = 60 - (start_min - end_min)
    else:
        minutes = end_min - start_min
    print(line[0], line[1], line[2], str(hour_diff) + ' hours', str(minutes) + ' minutes')