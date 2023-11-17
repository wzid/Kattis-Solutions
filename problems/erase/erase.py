n = int(input()) % 2
s = input()
s1 = input()

for i, c in enumerate(s1):
    if c != str((int(s[i]) + n) % 2):
        print('Deletion failed')
        exit()
print('Deletion succeeded')
        
