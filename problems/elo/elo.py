import sys
n, initial_elo = map(int, input().split())

opponents = []
for i in range(n):
    l, r, a = map(int, input().split())
    opponents.append((l, r, a))

dp = {}

def calculate_max_elo(curr_elo: int):
    if curr_elo in dp:
        return dp[curr_elo]
    
    dp[curr_elo] = curr_elo
    for i in range(n):
        if opponents[i][0] > curr_elo or curr_elo > opponents[i][1]:
            continue
        
        dp[curr_elo] = max(dp[curr_elo], calculate_max_elo(curr_elo + opponents[i][2]))
    
    return dp[curr_elo]

sys.setrecursionlimit(1500)
print(calculate_max_elo(initial_elo))