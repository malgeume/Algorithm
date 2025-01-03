import sys
arr = []
N = int(sys.stdin.readline())
for i in range(N):
    text = sys.stdin.readline()
    arr.append(text)
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)
for j in range(len(arr)):
    print(arr[j], end='')