n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(d)
print(array)
