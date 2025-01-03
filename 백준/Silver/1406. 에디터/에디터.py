import sys
s = list(sys.stdin.readline().rstrip())
word = []
M = int(sys.stdin.readline())
for i in range(M):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if s:
            word.append(s.pop())
    elif command[0] == 'D':
        if word:
            s.append(word.pop())
    elif command[0] == 'B':
    	if s:
            s.pop()  
    else:
    	s.append(command[1])
s.extend(reversed(word))
print(''.join(s))