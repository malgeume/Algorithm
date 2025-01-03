import sys
N = int(sys.stdin.readline())
for i in range(N):
    s = sys.stdin.readline().strip()
    if 6 <= len(s) <= 9:
        print("yes")
    else:
        print("no")