n, m = map(int, input().split())
x, y, direction = map(int, input().split())

visited = [[0] * m for _ in range(n)]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[x][y] = 1
count = 0
result = 1

while True:

    count += 1
    direction = (direction + 1) % 4

    nx = x + dx[direction]
    ny = y + dy[direction]

    if array[nx][ny] != 1 and visited[nx][ny] == 0 and 0 <= nx < m and 0 <= ny < n:
        x = nx
        y = ny
        count = 0
        result += 1
        visited[x][y] = 1
        continue

    if count == 4:
        x -= dx[direction]
        y -= dy[direction]

        count = 0

        if array[x][y] == 1:
            break

print(result)
