l,m,b=[*open(0)],0,set()
for x in map(int,l[2:]):
 if x in b:
  m+=1
  b={x}
 elif x>0:
  b|={x}
 else:
  b-={-x}
print(m)