N, M = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
value = 0
for k in range(N - 2):
    for j in range(k + 1, N - 1):
        for i in range(j + 1, N):
            total = arr[i] + arr[j] + arr[k]
            if value < total <= M:
                value = total
print(value)