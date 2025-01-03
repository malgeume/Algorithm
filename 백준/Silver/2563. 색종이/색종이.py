area = 0
n = int(input())
arr = [[0]*100 for i in range(100)]
for i in range(n):
    x_line, y_line = map(int, input().split())
    for y in range(10):
        for x in range(10):
            if arr[x_line + x][y_line + y] == 1:
                continue
            else:
                arr[x_line + x][y_line + y] = 1
for y in range(100):
    for x in range(100):
        if arr[x][y] == 1:
            area += 1
print(area)
