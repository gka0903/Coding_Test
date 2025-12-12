import sys

input = sys.stdin.readline
M, N = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
s, e = 1, max(l)
result = 0

while s <= e:
    m = (s + e) // 2
    cnt = 0

    for i in range(len(l)):
        if l[i] >= m:
            cnt += l[i] // m
        else:
            break

        if cnt >= M:
            break

    if cnt >= M:
        s = m + 1
        result = m
    else:
        e = m - 1

print(result)
