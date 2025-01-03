import sys

arr = list(sys.stdin.readline().strip())

if int(arr[0]) + int(arr[4]) == int(arr[8]):
    print("YES")
else:
    print("NO")