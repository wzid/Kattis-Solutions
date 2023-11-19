s = input()
zoom_level = len(s)

x, y = 0, 0
for i in range(zoom_level):
  digit = s[i]
  if digit == '1' or digit == '3':
    x += 2 ** (zoom_level - i - 1)
  if digit == '2' or digit == '3':
    y += 2 ** (zoom_level - i - 1)
print(zoom_level, x, y)