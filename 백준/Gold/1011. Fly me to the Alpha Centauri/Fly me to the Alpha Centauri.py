import sys
T = int(sys.stdin.readline())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    cnt = 0
    while True:
        if distance <= cnt * (cnt + 1):
            break
        cnt += 1
    if distance <= cnt ** 2:
        print(cnt * 2 - 1)
    
    else:
        print(cnt * 2)