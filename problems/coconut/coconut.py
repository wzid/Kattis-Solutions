# states = f: folded, s: split, p: 1 palm, sp: split and palm behind, pp: palm behind and palm down

s, n = map(int, input().split())
players = [[2, i+1] for i in range(n)]
s -= 1
ind = 0
while len(players) > 1:
    ind = (ind+s) % len(players)
    
    if players[ind][0] == 2:
        players[ind][0] = 1
        players.insert(ind, players[ind].copy())
    elif players[ind][0] == 1:
        players[ind][0] -= 1
        ind += 1
    else:
        players.pop(ind)


print(players[0][1])