k = int(input())

yours = input()
friend = input()

differences = 0

for i in range(len(yours)):
    if yours[i] != friend[i]:
        differences += 1

if differences == len(yours) and k > 0:
    print(len(yours) - k)
elif differences == len(yours) and k == 0:
    print(len(yours))
else:
    print(len(yours) - abs((len(yours) - differences) - k))