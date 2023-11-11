n = int(input())
winnings = sum(list(map(int, input().split())))
if winnings / 3 == winnings // 3:
    print('yes')
else:
    print('no')