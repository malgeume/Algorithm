import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

city = [[int(1e9) for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    city[a - 1][b - 1] = min(c, city[a - 1][b - 1])
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])
            city[i][i] = 0

for i in range(n):
    for j in range(n):
        if city[i][j] == int(1e9):
            city[i][j] = 0

for i in range(n):
    print(*city[i])