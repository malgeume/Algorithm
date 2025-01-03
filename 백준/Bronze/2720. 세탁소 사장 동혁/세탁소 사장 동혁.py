T = int(input())
for i in range(T):
    change = int(input())
    for j in [25, 10, 5, 1]:
        print(change // j, end=' ')
        change = change % j