import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
e = max(trees)
s = 0

while s <= e:
    mid = (s + e) // 2
    tree = 0
    for t in trees:
        if t - mid > 0:
            tree += t - mid

    if tree >= M:
        s = mid + 1
    elif tree < M:
        e = mid - 1

print(e)
