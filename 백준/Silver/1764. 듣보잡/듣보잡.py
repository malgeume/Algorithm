import sys
N, M = map(int, sys.stdin.readline().split())
hear = set()
see = set()
for i in range(N):
    hear.add(sys.stdin.readline().rstrip())
for j in range(M):
    see.add(sys.stdin.readline().rstrip())
all = list(hear & see)
all.sort()
print(len(all))
print(*all, sep='\n')