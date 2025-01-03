import sys
K, N = map(int, sys.stdin.readline().split())
arr = []
for i in range(K):
    arr.append(int(sys.stdin.readline()))
start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for j in arr:
        cnt += j // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)