from sys import stdin

for line in stdin:
    c, n = map(int, line.strip().split())
    items = []
    for i in range(n):
        v, w = map(int, stdin.readline().split())
        items.append((v, w))
    # n+1 so we have a buffer
    dp = [[0 for _ in range(c+1)]]

    for i_item in range(1, n+1):
        dp.append(dp[i_item-1].copy())
        value, weight = items[i_item - 1]
        for i_cap in range(weight, c+1):
            dp[i_item][i_cap] = max(dp[i_item][i_cap], value + dp[i_item-1][i_cap - weight])
    
    # Which items do we actually need to select
    # start by bottom right and work backwards
    # include an element if the current value and 
    # the value in the row above it differ
    i_cap = c
    selected_items = []
    for i_item in range(n, 0, -1):
        # this is an element where we have picked
        if dp[i_item][i_cap] != dp[i_item-1][i_cap]:
            # subtract weight
            selected_items.append(i_item-1)
            i_cap -= items[i_item - 1][1]
    
    print(len(selected_items))
    print(*selected_items)