blocks = int(input())

heights = sorted(list(map(int, input().split())), reverse=True)

# we would use a charge for each block
max_charges = blocks

# decision: find the minumum number of charges needed to decimate the blocks

# we would only want to use the massive charge on the tallest buildings
# does this matter

for i in range(blocks):
    max_charges = min(max_charges, heights[i]+i)

print(max_charges)