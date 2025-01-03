arr = []
for i in range(9):
    ary = list(map(int, input().split()))
    arr.append(ary)
max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= arr[row][col]:
            max_num = arr[row][col]
            max_row = row + 1
            max_col = col + 1
print(max_num)
print(max_row, max_col)
