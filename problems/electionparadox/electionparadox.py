
n = int(input())

regions = list(map(int, input().split()))

# Sort regions based on population (largest first)
regions.sort(reverse=True)

# Losing large regions
cutoff = (n - 1) // 2
losingLarge = regions[0:cutoff]
winningSmall = regions[cutoff:n]

# Total up votes
votes = 0
votes += sum(losingLarge)
for smallRegion in winningSmall:
    losingSmall = (smallRegion - 1) // 2
    votes += losingSmall
    
# Output
print(votes)