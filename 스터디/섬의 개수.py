import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def dfs(h, w, f, v, H, W):
    v[h][w] = True

    for dh, dw in d:
        nh = dh + h
        nw = dw + w

        if 0 <= nh < H and 0 <= nw < W:
            if not v[nh][nw] and f[nh][nw] == 1:
                dfs(nh, nw, f, v, H, W)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    field = []
    visit = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        line = list(map(int, input().split(" ")))
        field.append(line)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1 and not visit[i][j]:
                cnt += 1
                dfs(i, j, field, visit, h, w)

    print(cnt)
