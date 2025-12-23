import sys

input = sys.stdin.readline
H, W = map(int, input().split())
JOI = []

for i in range(H):
    s = input()
    row = [-1] * W
    current = -1

    for j in range(W):
        if current != -1:
            current += 1
            row[j] = current

        if s[j] == "c":
            row[j] = 0
            current = 0

    print(*row)
