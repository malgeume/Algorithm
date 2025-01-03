import sys
from collections import deque

def check(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs(row, col):
    global cnt
    dq = deque()
    dq.append((row, col))
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if check(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                if campus[nr][nc] == 'P':
                    cnt += 1
                elif campus[nr][nc] == 'X':
                    continue 
                dq.append((nr, nc))

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    campus = []
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        campus.append(list(sys.stdin.readline().strip()))

    for r in range(N):
        for c in range(M):
            if campus[r][c] == 'I':
                bfs(r, c)

    if cnt == 0:
        print("TT")
    else:
        print(cnt)