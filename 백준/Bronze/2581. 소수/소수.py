M = int(input())
N = int(input())
arr = []
count = 0
for i in range(M, N + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                arr.append(i)
            else:
                break
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))