import sys

N = int(sys.stdin.readline())

magnet = sys.stdin.readline().strip()

if "11" in magnet or "22" in magnet:
    print("No")
else:
    print("Yes")