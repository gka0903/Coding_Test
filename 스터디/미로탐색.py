import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cnt, result = 0, float('INF')

miro = []
for _ in range(N):
    row = list(map(int, input().rstrip()))
    miro.append(row)

visit = [[False for _ in range(M)] for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(n, m, cnt):
    global result

    visit[n][m] = True

    if n == N - 1 and m == M - 1:
        result = min(result, cnt)

    for y, x in dir:
        ny = n + y
        nx = m + x

        if 0 <= ny < N and 0 <= nx < M:
            if miro[ny][nx] == 1:
                if not visit[ny][nx]:
                    dfs(ny, nx, cnt + 1)

    visit[n][m] = False


dfs(0, 0, 1)

print(result)
