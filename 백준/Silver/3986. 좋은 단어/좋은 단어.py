N = int(input())
cnt = 0
for i in range(N):
    stack = []
    s = list(input())
    for j in range(len(s)):
        if len(stack) > 0:
            if s[j] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[j])
        else:
            stack.append(s[j])
    if len(stack) == 0:
        cnt += 1
print(cnt)