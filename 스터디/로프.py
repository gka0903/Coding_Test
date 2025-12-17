import sys

input = sys.stdin.readline
rope = []
N = int(input())

for i in range(N):
    rope.append(int(input()))

rope.sort()
s, e = 0, N - 1
cur_weight = 0

for i in range(N):
    cur_weight = max(cur_weight, (N - i) * rope[i])

print(cur_weight)
