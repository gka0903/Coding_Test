from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))

    return maps[n - 1][m - 1] if maps[n - 1][m - 1] > 1 else -1


print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1]]))
