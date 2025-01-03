import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
	arr = input().rstrip()
	password = []
	cursor = []
	for i in arr:
		if i == '<':
			if password:
				cursor.append(password.pop()) 
		elif i == '>':
			if cursor:
				password.append(cursor.pop())
		elif i == '-':
			if password:
				password.pop()
		else:
			password.append(i)
	print("".join(password),"".join(cursor[::-1]),sep="")