limit, events = map(int, input().split())

people = 0
unable = 0
for i in range(events):
    s = input().split()
    action = s[0]
    num_people = int(s[1])
    if action == 'enter':
        if people + num_people > limit:
            unable += 1
        else:
            people += num_people
    else:
        people -= num_people
print(unable)