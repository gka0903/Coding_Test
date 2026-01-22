import math
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
jewel = []


def check(mid):
    if mid == 0:
        return False
    cnt = 0

    for i in range(M):
        cnt += math.ceil(jewel[i] / mid)

    if cnt <= N:
        return True
    return False


for _ in range(M):
    jewel.append(int(input()))

s = 1
e = sum(jewel)
result = 0

while s <= e:
    m = (s + e) // 2

    if check(m):
        e = m - 1
        result = m
    else:
        s = m + 1

print(result)
