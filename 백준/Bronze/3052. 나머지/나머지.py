num=[]
for i in range(10):
    n = int(input())%42
    if n not in num:
        num.append(n)
print(len(num))