import sys

HH, MM = map(int, sys.stdin.readline().split())

hh = 9
mm = 0

time = (HH - hh) * 60 + MM - mm

print(time)