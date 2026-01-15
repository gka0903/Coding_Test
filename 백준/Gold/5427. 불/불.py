import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def fire():
    w, h = map(int, input().split())

    s_q = deque([])
    f_q = deque([])
    _map = []

    time = 0
    success = False

    for y in range(h):
        s = input().strip()
        row = []

        for x in range(w):
            row.append(s[x])

            if s[x] == "@":
                s_q.append((y, x))

            if s[x] == "*":
                f_q.append((y, x))

        _map.append(row)

    while s_q:
        s_len = len(s_q)
        f_len = len(f_q)

        time += 1

        for i in range(f_len):
            fy, fx = f_q.popleft()

            for j in range(4):
                nfy, nfx = fy + dy[j], fx + dx[j]

                if 0 <= nfy < h and 0 <= nfx < w:
                    if _map[nfy][nfx] == "." or _map[nfy][nfx] == "@":
                        _map[nfy][nfx] = "*"
                        f_q.append((nfy, nfx))

        for i in range(s_len):
            sy, sx = s_q.popleft()

            if sx == 0 or sx == w - 1 or sy == 0 or sy == h - 1:
                success = True
                s_q = []
                break

            for j in range(4):
                nsy, nsx = sy + dy[j], sx + dx[j]

                if 0 <= nsy < h and 0 <= nsx < w:
                    if _map[nsy][nsx] == ".":
                        _map[nsy][nsx] = "@"
                        s_q.append((nsy, nsx))

    if success:
        print(time)
    else:
        print("IMPOSSIBLE")


N = int(input())

for _ in range(N):
    fire()
