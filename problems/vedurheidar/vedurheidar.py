wind_speed = int(input())
n = int(input())
for i in range(n):
    s = input().split()
    if int(s[1]) < wind_speed:
        print(s[0], 'lokud')
    else:
        print(s[0], 'opin')
        