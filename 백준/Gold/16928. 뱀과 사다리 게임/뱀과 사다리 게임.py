import sys
from collections import deque

def bfs():
    dq = deque()
    dq.append(1)

    while dq:
        cell = dq.popleft()
        
        if cell == 100:
            print(cnt[100])
            break
        
        for i in range(1, 7):
            next = cell + i
            if next <= 100 and not visited[next]: 
                if next in ladder:
                    next = ladder[next]
                    if not visited[next]:
                        visited[next] = True
                        cnt[next] = cnt[cell] + 1
                        dq.append(next)
                        
                elif next in snake:
                    next = snake[next]
                    if not visited[next]:
                        visited[next] = True
                        cnt[next] = cnt[cell] + 1
                        dq.append(next)
                
                else:
                    visited[next] = True
                    cnt[next] = cnt[cell] + 1
                    dq.append(next)
                    
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    ladder = {}
    snake = {}

    visited = [False for _ in range(101)]
    cnt = [0 for _ in range(101)]

    for i in range(N):
        x, y = map(int, sys.stdin.readline().split())
        ladder[x] = y

    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        snake[u] = v
        
    bfs()