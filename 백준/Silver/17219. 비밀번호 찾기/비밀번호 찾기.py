import sys
N, M = map(int, sys.stdin.readline().split())
site = {}
for i in range(N):
    s, p = map(str, sys.stdin.readline().rstrip().split(' '))
    site[s] = p
    site[p] = s
for j in range(M):
    want = sys.stdin.readline().rstrip()
    print(site[want])