import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
value = [0]
sums = 0
for i in arr:
    sums += i
    value.append(sums)
for j in range(M):
    f, l = map(int, sys.stdin.readline().split())
    print(value[l] - value[f - 1])