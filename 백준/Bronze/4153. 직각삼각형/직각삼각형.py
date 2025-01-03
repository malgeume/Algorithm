while 1:
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break
    A *= A
    B *= B
    C *= C
    if A + B == C or A + C == B or B + C == A:
        print("right")
    else:
        print("wrong")