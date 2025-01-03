L = int(input())
sentence = input()
r = 31
M = 1234567891
H = 0
for i in range(L):
    H += (ord(sentence[i])-96) * (r**i)
print(H % M)