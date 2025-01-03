import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr = [0] * n
for i in range(n):
    for j in range(i):
        if A[i] > A[j] and arr[i] < arr[j]:
            arr[i] = arr[j]
    arr[i] += 1
print(max(arr))