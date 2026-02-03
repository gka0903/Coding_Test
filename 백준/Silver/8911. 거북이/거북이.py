import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    d = 0
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    l = [0, 0]
    r = [0, 0]

    cur_y = 0
    cur_x = 0

    commands = input()

    for c in commands:
        if c == "F" or c == "B":
            if c == "F":
                cur_y += dy[d]
                cur_x += dx[d]
            else:
                cur_y -= dy[d]
                cur_x -= dx[d]

            if l[0] > cur_x:
                l[0] = cur_x

            if l[1] < cur_y:
                l[1] = cur_y

            if r[0] < cur_x:
                r[0] = cur_x

            if r[1] > cur_y:
                r[1] = cur_y

        if c == "L":
            d -= 1

            if d == -1:
                d = 3

        if c == "R":
            d += 1

            if d == 4:
                d = 0

    print((r[0] - l[0]) * (l[1] - r[1]))
