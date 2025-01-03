N = int(input())
old = N
cycles = 0
while 1:
    a = N // 10
    b = N % 10
    c = (a + b) % 10
    N = b * 10 + c
    cycles += 1
    if old == N:
        break
print(cycles)