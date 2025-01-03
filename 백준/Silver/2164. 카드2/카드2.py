import sys
from collections import deque
N = int(sys.stdin.readline())
dq = deque()
for i in range(1, N + 1):
    dq.append(i)
for j in range(N - 1):
    dq.popleft()
    output = dq.popleft()
    dq.append(output)
print(dq[0])