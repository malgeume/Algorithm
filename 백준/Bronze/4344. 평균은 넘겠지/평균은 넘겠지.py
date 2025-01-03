C = int(input())
for i in range(C):
    count = 0
    arr = list(map(int, input().split()))
    average = sum(arr[1:]) / arr[0]
    for scores in arr[1:]:
        if scores > average:
            count += 1
    rate = count / arr[0]
    print(f"{rate:.3%}")