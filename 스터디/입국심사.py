import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
T = []

for i in range(N):
    T.append(int(input()))

s, e = 1, max(T) * M
result = -1

while s <= e:
    m = (s + e) // 2
    time = 0

    for i in range(N):
        time += m // T[i]

    if time >= M:
        e = m - 1
        result = m
    else:
        s = m + 1


print(result)
