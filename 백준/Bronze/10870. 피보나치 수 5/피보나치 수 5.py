n = int(input())
fib = [0, 1]
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    print(fib[n])