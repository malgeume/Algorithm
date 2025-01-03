N, M = map(int, input().split())
board = []
count = []
for i in range(N):
    board.append(input())
for x in range(N - 7):
    for y in range(M - 7):
        white = 0
        black = 0
        for r in range(x, x + 8):
            for c in range(y, y + 8):
                if (r + c) % 2 == 0:
                    if board[r][c] != 'W':
                        white += 1
                    if board[r][c] != 'B':
                        black += 1
                else:
                    if board[r][c] != 'B':
                        white += 1
                    if board[r][c] != 'W':
                        black += 1
        count.append(white)
        count.append(black)
print(min(count))