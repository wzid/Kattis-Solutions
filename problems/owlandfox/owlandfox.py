n = int(input())

for i in range(n):
    x = input()
    for reverse_i, cipher in enumerate(reversed(x)):
        cipher = int(cipher)
        if cipher != 0:
            index = len(x) - reverse_i - 1
            prev = x[:index] + str(cipher - 1) + x[index + 1:]
            print(int(prev))
            break