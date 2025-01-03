import sys

def wave(N):
    if arr[N]:
        return arr[N]
    else:
        arr[N] = wave(N - 2) + wave(N - 3)
        return arr[N]

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    arr = [0] * 101
    arr[1] = 1
    arr[2] = 1
    arr[3] = 1
    for i in range(T):
        N = int(sys.stdin.readline())
        print(wave(N))