R, C = map(int, input().split())
arr = [[0 for i in range(2 * C)] for j in range(2 * R)]
for i in range(R):
    word = input()
    for j in range(C):
        arr[i][j] = word[j]
        arr[i][-1 - j] = word[j]
        arr[-1 - i][j] = word[j]
        arr[-1 - i ][-1 - j] = word[j]
x, y = map(int, input().split())
if arr[x - 1][y - 1] == ".":
    arr[x - 1][y - 1] = "#"
else:
    arr[x - 1][y - 1] = "."
for i in range(2 * R):
    print("".join(arr[i]))