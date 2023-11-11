n, h, v = map(int, input().split())

first_area = h*v
second_area = h*(n-v)
third_area = (n-h)*v
fourth_area = (n-h)*(n-v)

print(max(first_area, second_area, third_area, fourth_area)*4)