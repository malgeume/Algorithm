T = int(input())
for i in range(T):
    k = int(input())
    n = int(input()) 
    people = [x for x in range(1, n+1)]
    for floor in range(k):
        for room in range(1, n):
            people[room] += people[room-1]
    print(people[n-1])