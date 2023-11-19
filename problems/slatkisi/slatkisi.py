c, k = map(int, input().split())

bill = int('1' + '0'*k)

print(round(c/bill) * bill)