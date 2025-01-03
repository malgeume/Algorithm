import sys
n = int(sys.stdin.readline())
stack = []
calculation = []
flag = True
cnt = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        stack.append(cnt)
        calculation.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        calculation.append('-')
    else:
        flag = False
if not flag:
    print("NO")
else:
    for j in calculation:
        print(j)