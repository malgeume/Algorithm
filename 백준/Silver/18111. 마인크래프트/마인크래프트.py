import sys

N, M, B = map(int, sys.stdin.readline().split())

ground = []
time = int(1e9)
height = 0

for i in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))

for h in range(257):
    obtained_blocks = 0
    used_blocks = 0
    
    for i in ground:
        for j in i:
            if j > h:
                obtained_blocks += j - h
            else:
                used_blocks += h - j
                
    if obtained_blocks + B >= used_blocks:
        if obtained_blocks * 2 + used_blocks <= time:
            time = obtained_blocks * 2 + used_blocks
            height = h

print(time, height)