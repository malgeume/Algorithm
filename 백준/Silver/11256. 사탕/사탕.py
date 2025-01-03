import sys
T = int(sys.stdin.readline())
for i in range(T):
    box = []
    cnt = 0
    J, N = map(int, sys.stdin.readline().split())
    for j in range(N):
        R, C = map(int, sys.stdin.readline().split())
        box.append(R * C)
    box.sort(reverse = True)
    for k in box:
        J -= k
        cnt += 1
        if J <= 0:
            break
    print(cnt)