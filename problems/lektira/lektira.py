x=input()
print(min(x[:i][::-1]+x[i:j][::-1]+x[j:][::-1]for i in range(1,len(x)-2)for j in range(i+2,len(x))))