import copy
import sys

input = sys.stdin.readline

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
F = [[] for _ in range(4)]

for a in range(4):
    li = list(map(int, input().split()))

    # index 값으로 방향 받기
    # 번호, 방향
    for b in range(0, len(li), 2):
        F[a].append([li[b], li[b + 1] - 1])


def dfs(field, ys, xs, mount):
    global result
    result = max(mount, result)

    for f in range(1, 17):
        f_y, f_x = -1, -1
        for i in range(4):
            for j in range(4):
                if field[i][j][0] == f:
                    f_y, f_x = i, j
                    break
            if f_y != -1:
                break

        if f_y == -1:
            continue

        f_d = field[f_y][f_x][1]

        for i in range(8):
            nd = (f_d + i) % 8
            ny = f_y + dy[nd]
            nx = f_x + dx[nd]

            if 0 <= ny < 4 and 0 <= nx < 4:
                if not (ny == ys and nx == xs):
                    field[f_y][f_x][1] = nd
                    field[f_y][f_x], field[ny][nx] = field[ny][nx], field[f_y][f_x]
                    break

    shark_dir = field[ys][xs][1]

    for s in range(1, 4):
        ny = ys + dy[shark_dir] * s
        nx = xs + dx[shark_dir] * s

        if 0 <= ny < 4 and 0 <= nx < 4:
            if field[ny][nx][0] > 0:
                new_F = copy.deepcopy(field)

                new_score = new_F[ny][nx][0]
                new_F[ny][nx][0] = -1
                new_F[ys][xs][0] = 0

                dfs(new_F, ny, nx, mount + new_score)


result = 0
first_fish_score = F[0][0][0]
F[0][0][0] = -1

dfs(F, 0, 0, first_fish_score)

print(result)
