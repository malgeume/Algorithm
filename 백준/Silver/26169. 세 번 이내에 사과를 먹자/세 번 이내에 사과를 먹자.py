import sys

def DFS(y, x, depth, cnt):
    visited[y][x] = True
    if board[y][x] == 1:
        cnt += 1
    if 2 <= cnt:
        return 1
    if 2 < depth:
        visited[y][x] = False
        return 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            if not visited[ny][nx] and board[ny][nx] != -1:
                if DFS(ny, nx, depth + 1, cnt) == 1:
                    return 1
    visited[y][x] = False
    return 0

if __name__ == "__main__":
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    board = [list(map(int, input().split())) for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    r, c = map(int, input().split())
    print(DFS(r, c, 0, 0))