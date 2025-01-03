A = list(map(int, input().split()))
result = 0
for i in range(len(A)):
    result += A[i]**2
print(result%10)