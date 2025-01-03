N, K = map(int, input().split())
def bin(N, K):
    if K == 0 or N == K:
        return 1
    else:
        return bin(N - 1, K - 1) + bin(N - 1, K)
print(bin(N, K))