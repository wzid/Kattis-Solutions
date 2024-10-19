start = 5

def is_leap_year(n):
    if n % 100 == 0:
        return n % 400 == 0
    return n % 4 == 0
x = int(input())

s = 0
for i in range(2000, x):
    s += 365 + is_leap_year(i)

index = start + s
index += 31 + 28 + 31 + 30
if is_leap_year(x):
    index += 1
index %= 7

diff_from_first_sunday = 6 - index

mothers_day = diff_from_first_sunday + 7

index += 31
ind_copy = index
index %= 7

diff_from_first_sunday_june = 6 - index

fathers_day = diff_from_first_sunday_june + 14 + 31

diff = fathers_day - mothers_day

print(f'{diff // 7} weeks')