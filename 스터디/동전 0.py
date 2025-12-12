import sys

input = sys.stdin.readline
stack = []
N, K = map(int, input().split())

for i in range(N):
    stack.append(int(input()))

cnt = 0
while stack and K >= 0:
    n = stack.pop()

    if K >= n:
        c = K // n
        K -= n * c
        cnt += c

print(cnt)
