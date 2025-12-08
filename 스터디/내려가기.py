import sys

input = sys.stdin.readline
N = int(input())
max_cur = [0] * 3
min_cur = [0] * 3

for _ in range(N):
    max_prev = max_cur
    min_prev = min_cur
    cur = list(map(int, input().split()))
    max_cur = cur[:]
    min_cur = cur[:]

    for i in range(len(max_cur)):
        if len(max_cur) >= 2:
            if i == 0:
                max_cur[i] = max(max_prev[i], max_prev[i + 1]) + max_cur[i]
                min_cur[i] = min(min_prev[i], min_prev[i + 1]) + min_cur[i]
                continue
            elif i == len(max_cur) - 1:
                max_cur[i] = max(max_prev[i], max_prev[i - 1]) + max_cur[i]
                min_cur[i] = min(min_prev[i], min_prev[i - 1]) + min_cur[i]
                continue

        max_cur[i] = max(max_prev[i + 1], max_prev[i], max_prev[i - 1]) + max_cur[i]
        min_cur[i] = min(min_prev[i + 1], min_prev[i], min_prev[i - 1]) + min_cur[i]

print(max(max_cur), end=" ")
print(min(min_cur))
