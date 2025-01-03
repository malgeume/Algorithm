import sys
arr = []
N = int(sys.stdin.readline())
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for j in range(N):
    print(arr[j])