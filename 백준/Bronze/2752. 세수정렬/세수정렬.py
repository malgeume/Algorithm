import sys

arr = list(map(int, sys.stdin.readline().split()))

print(*sorted(arr))