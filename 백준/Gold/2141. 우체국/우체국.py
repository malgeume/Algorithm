import sys
N = int(sys.stdin.readline())
village = []
people = 0
cnt = 0
post = 0
for i in range(N):
    X, A = map(int, sys.stdin.readline().split())
    village.append((X, A))
village.sort(key = lambda x : x[0])
for j in village:
    people += j[1]
mid = people // 2
if people % 2 != 0:
    mid += 1
for k in village:
    cnt += k[1]
    if cnt >= mid:
        print(k[0])
        break