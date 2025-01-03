T = int(input())
for i in range(T):
    stack = []
    s = input()
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")