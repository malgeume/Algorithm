import sys
from collections import deque, defaultdict

N, M, K = map(int, sys.stdin.readline().split())

cnt = 0
earth = [[5] * N for _ in range(N)]
nutrient = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
age = [[deque() for _ in range(N)] for _ in range(N)]
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# 초기 나무 상태 입력
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    age[x - 1][y - 1].append(z)

# 시뮬레이션
for _ in range(K):
    new_trees = defaultdict(int)  # 가을에 번식할 나무 위치 저장

    # 1. 봄
    for r in range(N):
        for c in range(N):
            if not age[r][c]:
                continue
            
            live = deque()
            dead_nutrient = 0
            
            # 어린 나무부터 처리
            while age[r][c]:
                tree = age[r][c].popleft()
                if earth[r][c] >= tree:
                    earth[r][c] -= tree
                    live.append(tree + 1)
                    # 번식 가능한 나무 체크
                    if (tree + 1) % 5 == 0:
                        new_trees[(r, c)] += 1
                else:
                    dead_nutrient += tree // 2
            
            # 살아있는 나무와 죽은 나무 처리
            age[r][c] = live
            earth[r][c] += dead_nutrient

    # 2. 가을 - 나무 번식
    for (r, c), count in new_trees.items():
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                age[nr][nc].extendleft([1] * count)  # 어린 나무를 앞에 추가

    # 3. 겨울 - 양분 추가
    for r in range(N):
        for c in range(N):
            earth[r][c] += nutrient[r][c]

# 결과 계산
cnt = sum(len(age[r][c]) for r in range(N) for c in range(N))
print(cnt)
