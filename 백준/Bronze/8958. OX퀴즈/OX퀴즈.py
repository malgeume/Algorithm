T=int(input())
for i in range(T):
    A=input()
    n=0
    num=1
    for i in A:
        if i=="O":
            n+=num
            num+=1
        else:
            n+=0
            num=1
    print(n)