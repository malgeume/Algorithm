import sys
S = set()
M = int(sys.stdin.readline())
for i in range(M):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        command[1] = int(command[1])
    if command[0] == "add":
        if command[1] not in S:
            S.add(command[1])
    elif command[0] == "remove":
        if command[1] in S:
            S.discard(command[1])
    elif command[0] == "check":
        if command[1] in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in S:
            S.discard(command[1])
        else:
            S.add(command[1])
    elif command[0] == "all":
        S = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        S = set()