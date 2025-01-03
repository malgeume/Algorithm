N, M = input().split()
N = N[::-1]
M = M[::-1]
if N > M:
    print(N)
else:
    print(M)