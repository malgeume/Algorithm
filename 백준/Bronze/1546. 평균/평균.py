N = int(input())
A = list(map(int, input().split()))
M = max(A)
aver = 0
for i in A:
    aver += i/M*100
print(aver/N)