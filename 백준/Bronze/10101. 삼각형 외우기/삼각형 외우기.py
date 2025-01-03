arr = []
for i in range(3):
    ang = int(input())
    arr.append(ang)
if arr.count(60) == 3:
    print('Equilateral')
elif sum(arr) == 180 and len(set(arr)) == 2:
    print('Isosceles')
elif sum(arr) == 180 and len(set(arr)) == 3:
    print('Scalene')
else:
    print('Error')