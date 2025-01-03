import sys

N, L = map(int, sys.stdin.readline().split())

guidance = []

for _ in range(N):
    guidance.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
visited = [[False for _ in range(N)] for _ in range(N)]

for r in range(N):
    now = 0

    while 1:
        if now == N - 1:
            cnt += 1
            break
        if guidance[r][now] == guidance[r][now + 1]:
            now += 1
            continue
        elif abs(guidance[r][now] - guidance[r][now + 1]) > 1:
            break
        else:
            if guidance[r][now] - guidance[r][now + 1] == 1:
                flag = False
                for i in range(1, L + 1):
                    if 0 <= now + i < N:
                        if not visited[r][now + i]:
                            if guidance[r][now + 1] == guidance[r][now + i]:
                                flag = True
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                    
                if flag:
                    for i in range(1, L + 1):
                        visited[r][now + i] = True
                    now += L
                else:
                    break

            elif guidance[r][now] - guidance[r][now + 1] == -1:
                flag = False
                for i in range(0, L):
                    if 0 <= now - i < N:
                        if not visited[r][now - i]:
                            if guidance[r][now] == guidance[r][now - i]:
                                flag = True
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                
                if flag:
                    for i in range(0, L):
                        visited[r][now - i] = True
                    now += 1
                else:
                    break

visited = [[False for _ in range(N)] for _ in range(N)]
for c in range(N):
    now = 0

    while 1:
        if now == N - 1:
            cnt += 1
            break
        if guidance[now][c] == guidance[now + 1][c]:
            now += 1
            continue
        elif abs(guidance[now][c] - guidance[now + 1][c]) > 1:
            break
        else:
            if guidance[now][c] - guidance[now + 1][c] == 1:
                flag = False
                for i in range(1, L + 1):
                    if 0 <= now + i < N:
                        if not visited[now + i][c]:
                            if guidance[now + 1][c] == guidance[now + i][c]:
                                flag = True
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                    
                if flag:
                    for i in range(1, L + 1):
                        visited[now + i][c] = True
                    now += L
                else:
                    break

            elif guidance[now][c] - guidance[now + 1][c] == -1:
                flag = False
                for i in range(0, L):
                    if 0 <= now - i < N:
                        if not visited[now - i][c]:
                            if guidance[now][c] == guidance[now - i][c]:
                                flag = True
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                
                if flag:
                    for i in range(0, L):
                        visited[now - i][c] = True
                    now += 1
                else:
                    break

print(cnt)