import sys
N = int(sys.stdin.readline())
students = []
for i in range(N):
    students.append(list(sys.stdin.readline().split()))
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for j in students:
    print(j[0])