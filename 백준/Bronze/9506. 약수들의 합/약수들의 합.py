while 1:
    N = int(input())
    if N == -1:
        break
    arr = []
    for i in range(1,N):
        if N % i == 0:
            arr.append(i)
    if sum(arr) == N:
        print(N, '=', end=' ')
        print(*arr, sep=' + ')
    else:
        print(N, "is NOT perfect.")
