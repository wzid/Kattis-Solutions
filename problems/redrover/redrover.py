s = input()
mmin = len(s)
for i in range(len(s)):
    for j in range(i+1, len(s)):
        t = s[i:j]
        replaced = s.replace(t, "M")
        mmin = min(mmin, len(replaced) + len(t))

print(mmin)