import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
dic = {}
for i in A:
  if i in dic :
    dic[i] += 1
  else:
    dic[i] = 1
for j in B:
  if j in dic:
    print(dic[j], end=' ')
  else:
    print('0', end=' ')