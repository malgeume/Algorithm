import sys
import math
cnt = 0
N = int(sys.stdin.readline())
fact = math.factorial(N)
fact = list(map(int, str(fact)))
for i in range(len(fact) - 1, -1, -1):
    if fact[i] == 0:
        cnt += 1
    else:
        break
print(cnt)