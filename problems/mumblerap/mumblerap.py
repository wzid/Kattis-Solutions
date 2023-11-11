length = int(input())
s = input()
num_found = False
num = ''
largest = 0
for c in s:
    if c.isnumeric():
        if num_found:
            num += c
        else:
            num_found = True
            num = c
    elif num_found:
        largest = max(int(num), largest)
        num_found = False
if num_found:
    largest = max(int(num), largest)
print(largest)