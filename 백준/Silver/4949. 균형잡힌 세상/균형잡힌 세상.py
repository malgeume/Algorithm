while 1:
    s = list(input())
    stack = []
    if s[0] == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    if not stack:
        print('yes')
    else:
        print('no')