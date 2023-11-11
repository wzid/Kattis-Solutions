l = input()
smile = l.count(':)')
sad = l.count(':(')

if smile and not sad:
    print('alive')
elif sad and not smile:
    print('undead')
elif sad and smile:
    print('double agent')
else:
    print('machine')