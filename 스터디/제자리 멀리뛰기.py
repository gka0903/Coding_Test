import sys

input = sys.stdin.readline
d, n, m = map(int, input().split())
lands = []

for i in range(n):
    r = int(input())
    lands.append(r)
lands.sort()

s = 1
e = d
target = None

while s <= e:
    mid = (s + e) // 2
    prev = 0
    cnt = 0

    for r in lands:
        dist = r - prev

        if dist < mid:
            cnt += 1
        else:
            prev = r

    if cnt <= m:
        s = mid + 1
        target = mid
    else:
        e = mid - 1

print(target)
