import sys

def seq():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in arr:
        if i in s:
            continue
        else:
            s.append(i)
            seq()
            s.pop()
            

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    s = []
    seq()