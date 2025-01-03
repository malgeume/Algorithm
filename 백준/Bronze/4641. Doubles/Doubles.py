cnt = 0
while 1:
    arr = list(map(int, input().split()))
    if -1 in arr:
        break
    for i in range(len(arr) - 1):
        if arr[i] * 2 in arr:
            cnt += 1
    print(cnt)
    cnt = 0