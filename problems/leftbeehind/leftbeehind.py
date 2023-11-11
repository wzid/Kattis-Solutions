while True:
    sweet, sour = map(int, input().split())
    if sweet == 0 and sour == 0:
        break
    
    if sour + sweet == 13:
        print('Never speak again.')
    elif sour > sweet:
        print('Left beehind.')
    elif sour < sweet:
        print('To the convention.')
    else:
        print('Undecided.')
    