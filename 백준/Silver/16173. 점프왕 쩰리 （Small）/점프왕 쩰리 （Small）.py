import sys

def DFS(a, b):
    global flag
    if a < 0 or a >= N or b < 0 or b >= N:
        return
    if visited[a][b]:
        return
    if arr[a][b] == -1:
        flag = True
        return
    visited[a][b] = True
    step = arr[a][b]
    DFS(a + step, b)
    DFS(a, b + step)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    flag = False
    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    visited = [[False] * N for _ in range(N)]
    DFS(0, 0)
    if flag:
        print("HaruHaru")
    else:
        print("Hing")