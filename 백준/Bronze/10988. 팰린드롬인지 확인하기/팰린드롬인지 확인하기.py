word = input()
answer = 0
if word == word[::-1]:
    answer = 1
else:
    answer = 0
print(answer)
