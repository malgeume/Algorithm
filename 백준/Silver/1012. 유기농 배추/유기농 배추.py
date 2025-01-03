import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M): 
            if cabbage[nx][ny] == 1: 
                cabbage[nx][ny] = -1 
                dfs(nx, ny)

T = int(sys.stdin.readline()) 
for i in range(T): 
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage = [[0 for i in range(M)] for j in range(N)]
    cnt = 0
    for i in range(K):
        m, n = map(int, sys.stdin.readline().split())
        cabbage[n][m] = 1 
    for i in range(N):
    	for j in range(M):
            if cabbage[i][j] > 0:
                dfs(i, j)
                cnt += 1 
    print(cnt)