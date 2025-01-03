arr = []
exc1 = 0
exc2 = 0
for i in range(9):
    arr.append(int(input()))
for i in range(8):
    for j in range(i + 1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            exc1 = arr[i]
            exc2 = arr[j]
            break
arr.remove(exc1)
arr.remove(exc2)
arr.sort()
for k in range(7):
    print(arr[k])