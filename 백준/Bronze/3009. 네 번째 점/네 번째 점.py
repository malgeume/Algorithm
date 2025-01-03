xlist = []
ylist = []
for i in range(3):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
for i in range(3):
    if xlist.count(xlist[i]) == 1:
        pointX = xlist[i]
    if ylist.count(ylist[i]) == 1:
        pointY = ylist[i]
print(pointX, pointY)