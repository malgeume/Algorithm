T = int(input())
for i in range(T):
    point = list(map(int, input().split()))
    point.remove(max(point))
    point.remove(min(point))
    if max(point)-min(point)>=4:
        print("KIN")
    else:
        print(sum(point))