import sys
n = int(sys.stdin.readline())
glass = []
wine = [0] * n
for i in range(n):
    glass.append(int(sys.stdin.readline()))
wine[0] = glass[0]
if n > 1:
    wine[1] = glass[0] + glass[1]
if n > 2:
    wine[2] = max(glass[2] + glass[0], glass[2] + glass[1], wine[1])
for j in range(3, n):
    wine[j]  = max(wine[j - 3] + glass[j - 1] + glass[j], wine[j - 2] + glass[j], wine[j - 1])
print(max(wine))