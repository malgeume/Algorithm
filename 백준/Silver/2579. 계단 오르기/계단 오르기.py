import sys
n = int(sys.stdin.readline())
stairs = []
score = [0] * n
for i in range(n):
    stairs.append(int(sys.stdin.readline()))
if n <= 2:
    print(sum(stairs))
else:
    score[0] = stairs[0]
    score[1] = stairs[0] + stairs[1]
    for j in range(2, n):
        score[j]  = max(score[j - 3] + stairs[j - 1] + stairs[j], score[j - 2] + stairs[j])
    print(score[-1])