import sys
T = int(sys.stdin.readline())
for i in range(T):
    clothes = {}
    n = int(sys.stdin.readline())
    cnt = 1
    for j in range(n):
        a, b = map(str, sys.stdin.readline().split())
        if b not in clothes:
            clothes[b] = 1
        else:
            clothes[b] += 1
    for i in clothes:
        cnt *= (clothes[i] + 1)
    print(cnt - 1)