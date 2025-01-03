import sys
N = int(sys.stdin.readline())
if N == 0:
    print("divide by zero")
else:
    prac = list(map(int, sys.stdin.readline().split()))
    ans = (sum(prac) / N) / (sum(prac) / N)
    print("%.2f" % ans)