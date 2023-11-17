x = sum(map(int,input().split()))
y = sum(map(int,input().split()))

if x>y:
  print("Gunnar")
elif x<y:
  print("Emma")
else:
  print("Tie")