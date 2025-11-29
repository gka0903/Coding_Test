from collections import deque


def solution(maps):
    answer = 0
    n, m = len(maps[0]), len(maps)
    q = deque([[(0, 0)]])
    d = ((0, 1), (1, 0), (-1, 0), (0, -1),)
    visit = [[False for _ in range(n)] for _ in range(m)]

    while q:
        current_chars = q.popleft()
        new_chars = []
        answer += 1

        for cy, cx in current_chars:
            dy, dx = cy, cx

            if dy == m - 1 and dx == n - 1:
                return answer

            for y, x in d:
                ny, nx = dy + y, dx + x

                if 0 <= ny < m and 0 <= nx < n and not visit[ny][nx] and maps[ny][nx] == 1:
                    new_chars.append((ny, nx))
                    visit[ny][nx] = True

        if new_chars:
            q.append(new_chars)

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
