s = input()
n = len(s) // 2
first, second = s[:n], s[n:]
rotation = sum([ord(c) - 65 for c in first])

res_first = ''
for c in first:
    res_first += chr((((ord(c) - 65) + rotation) % 26) + 65)

rotation = sum([ord(c) - 65 for c in second])

res_second = ''
for c in second:
    res_second += chr((((ord(c) - 65) + rotation) % 26) + 65)

res = ''
for i in range(len(res_first)):
    f_value = ord(res_first[i]) - 65
    s_value = ord(res_second[i]) - 65
    res += chr(((f_value + s_value) % 26) + 65)
print(res)