import sys

n = int(sys.stdin.readline())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

for r in range(1, n):
    for c in range(len(triangle[r])):
        if c == 0:
            triangle[r][c] = triangle[r - 1][c] + triangle[r][c]
        elif c == len(triangle[r]) - 1:
            triangle[r][c] = triangle[r - 1][c - 1] + triangle[r][c]
        else:
            triangle[r][c] = max(triangle[r - 1][c - 1], triangle[r - 1][c]) + triangle[r][c]

print(max(triangle[n - 1]))