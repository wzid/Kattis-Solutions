g, s, c = map(int, input().split())
buying_power = g*3 + s*2 + c


if buying_power >= 6:
    if buying_power < 8:
        print('Duchy or Gold')
    else:
        print('Province or Gold')
elif buying_power >= 3:
    if buying_power < 5:
        print('Estate or Silver')
    else:
        print('Duchy or Silver')
else:
    if buying_power < 2:
        print('Copper')
    else:
        print('Estate or Copper')