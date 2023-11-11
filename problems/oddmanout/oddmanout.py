n = int(input())
for i in range(n):
    input()
    g = list(map(int, input().rstrip().split()))
    odd_man_out = min(g, key=g.count)
    print(f'Case #{i+1}: {odd_man_out}')