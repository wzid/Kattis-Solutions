days_back = int(input())
days = []
for i in range(days_back):
    days.append(int(input()))

money = 100
for i in range(len(days)-1):
    if days[i+1] > days[i]:
        # can be at most 100000
        amount_can_buy = min(money//days[i], 100000)
        change = days[i+1] - days[i]
        money += amount_can_buy*change

print(money)