import sys
num = int(sys.stdin.readline())
arr = list(map(int, str(num)))
arr.sort()
for j in range(len(arr) - 1, -1, -1):
    print(arr[j], end='')