while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if sum((a, b, c)) - max(a, b, c) <= max(a, b, c):
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == c or b == c or a == b:
        print('Isosceles')
    else:
        print('Scalene')