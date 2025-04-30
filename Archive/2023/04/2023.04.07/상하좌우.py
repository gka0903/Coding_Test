n = int(input())
plans = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move = ['L', 'R', 'U', 'D']

for plan in plans:
    for index in range(len(move)):
        if plan == move[index]:
            nx = x + dx[index]
            ny = y + dy[index]
            break
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)
