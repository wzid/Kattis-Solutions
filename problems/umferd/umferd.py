width = int(input())
height = int(input())

dot_count = 0

for i in range(height):
    dot_count += input().count('.')

print(dot_count/(width*height))