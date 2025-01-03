import sys
a, b = sys.stdin.readline().split()
len_a, len_b = len(a), len(b)
if len_a >len_b:
    b = '0' * (len_a - len_b) + b
else:
    a = '0' * (len_b - len_a) + a
res = ""
for i in range(len(a)):
    res += str(int(a[i]) + int(b[i]))
print(res)