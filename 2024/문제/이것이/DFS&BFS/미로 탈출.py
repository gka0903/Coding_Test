from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().strip()))
    maze.append(row)

queue = deque()
queue.append((0, 0))

result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def add_array(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if maze[ny][nx] == 0:
            continue

        if maze[ny][nx] == 1:
            maze[ny][nx] = maze[y][x] + 1
            queue.append((ny, nx))


while queue:
    y, x = queue.popleft()
    add_array(y, x)

print(maze[n - 1][m - 1])
