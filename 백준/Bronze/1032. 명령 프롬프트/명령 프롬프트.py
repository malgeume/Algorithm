N = int(input())
word = list(input())
for i in range(N-1):
    other = input()
    for j in range(len(word)):
        if word[j] == other[j]:
            continue
        else:
            word[j] = "?"
print("".join(word))