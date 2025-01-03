form = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())
line = ''
while n:
    line += str(form[n%b])
    n //= b
print(line[::-1])