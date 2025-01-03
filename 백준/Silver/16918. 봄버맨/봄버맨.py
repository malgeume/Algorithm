import sys
import copy
R, C, N = map(int, sys.stdin.readline().split())
bomb = []
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
splash = []
for i in range(R):
    bomb.append(list(input()))
for j in range(0, N + 1):
    if j == 0:
        splash = copy.deepcopy(bomb)
        continue
    if j == 1:
        continue
    elif j % 2 == 0:
        splash = [['O' for i in range(C)] for j in range(R)]
    elif j % 2 == 1:
        for k in range(R):
            for l in range(C):
                if bomb[k][l] == 'O':
                    splash[k][l] = '.'
                    for m in range(4):
                        nx = l + dx[m]
                        ny = k + dy[m]
                        if 0 <= nx < C and 0 <= ny < R:
                            splash[ny][nx] = '.'
        bomb = copy.deepcopy(splash)
for o in range(R):
    print(*splash[o], sep='')