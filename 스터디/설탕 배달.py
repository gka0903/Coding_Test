import sys

input = sys.stdin.readline
N = int(input())
M = N // 5
result = [N] * (M + 1)

for i in range(M, -1, -1):
    d = N - i * 5

    if d % 3 == 0:
        result[i] = i + d // 3

r = min(result)
if r == N:
    print(-1)
else:
    print(r)
