import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())


def solution():
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    def dfs(y, x):
        visit[y][x] = True

        for dy, dx in d:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if not visit[ny][nx] and field[ny][nx] == 1:
                    dfs(ny, nx)

    cnt = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visit[y][x]:
                cnt += 1
                dfs(y, x)

    print(cnt)


for i in range(T):
    solution()
