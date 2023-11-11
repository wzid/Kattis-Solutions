m = {1: 31, 2: 28, 3: 31, 
     4: 30, 5: 31, 6: 30,
      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }


week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day, month = map(int, input().split())

d = 3
s = 0

for j in range(1, month):
    if j == month:
        break

    s += m[j]

s = day + s

for i in range(1, 366):
    if d == 7:
        d = 0
    
    if i == s:
        print(week[d])
        break

    d += 1
