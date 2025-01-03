words = []
len_word = 0
line = ''
for i in range(5):
    word = input()
    words.append(word)
    if len_word < len(word):
        len_word = len(word)

for col in range(len_word):
    for row in range(5):
        if col < len(words[row]):
            line += words[row][col]
print(line)