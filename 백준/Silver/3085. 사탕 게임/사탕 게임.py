import sys
N = int(sys.stdin.readline())
candy = []
value = 1
num = 1
def count():
    for l in range(N):
        global value
        cnt = 1 
        for m in range(N - 1):
            if candy[l][m] == candy[l][m + 1]:
                cnt += 1
            else:
                cnt = 1
            value = max(value, cnt)
        cnt = 1
        for m in range(N - 1):
            if candy[m][l] == candy[m + 1][l]:
                cnt += 1
            else:
                cnt = 1
            value = max(value, cnt)
    return value

for i in range(N):
    candy.append(list(sys.stdin.readline().rstrip()))
for j in range(N):
    for k in range(N):
        if k + 1 < N and candy[j][k] != candy[j][k + 1]:
            candy[j][k], candy[j][k + 1] = candy[j][k + 1], candy[j][k]
            count()
            num = max(value, num)
            candy[j][k], candy[j][k + 1] = candy[j][k + 1], candy[j][k]
        if j + 1 < N and candy[j][k] != candy[j + 1][k]:
            candy[j][k], candy[j + 1][k] = candy[j + 1][k], candy[j][k]
            count()
            num = max(value, num)
            candy[j][k], candy[j + 1][k] = candy[j + 1][k], candy[j][k]      
print(num)