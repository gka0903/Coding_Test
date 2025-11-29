# 입력 예시
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

import sys

# 입력
N = int(sys.stdin.readline())
# 그래프 만들고
graph = []
for _ in range(N):
    line = input().strip()
    graph.append(list(map(int, line)))

# 마을 수
# 집 수
# 방향
cnt = 0
house = 0
houses = []
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


# dfs 만들고
def dfs(x, y):
    global house

    # visit 처리
    graph[y][x] = 0
    house += 1

    # 4 direction search
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] == 1:
                dfs(nx, ny)


# 전체 탐색
for j in range(N):
    for i in range(N):
        if graph[j][i] == 1:
            house = 0
            dfs(i, j)
            houses.append(house)
            cnt += 1

# 답 출력
print(cnt)
houses.sort()
for h in houses:
    print(h)
