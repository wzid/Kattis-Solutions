t = int(input())

# d = dict, starting_point = int

for i in range(t):
    directions = {}
    dp = {}
    s = int(input())
    for j in range(s):
        inp = input().split()
        page_num = int(inp[0])

        if inp[1] == 'favourably':
            dp[page_num] = 1
        elif inp[1] == 'catastrophically':
            dp[page_num] = 0
        else:
            directions[page_num] = list(map(int, inp[1:]))
    
    def calc_endings(starting_point):
        if starting_point in dp:
            return dp[starting_point]
        else:
            tmp = directions[starting_point]
            fav_endings = calc_endings(tmp[0]) + calc_endings(tmp[1]) + calc_endings(tmp[2])
            dp[starting_point] = fav_endings
            return fav_endings
        
    endings = calc_endings(1)
    print(endings)