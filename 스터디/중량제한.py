import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N, M = map(int, input().split())
lands = [i for i in range(1, N + 1)]
s, e = 1000000000, 0
d = defaultdict(list)
result = -1

for i in range(M):
    A, B, C = map(int, input().split())
    s = min(s, C)
    e = max(e, C)
    d[A].append((B, C))
    d[B].append((A, C))

t1, t2 = map(int, input().split())

while s <= e:
    m = (s + e) // 2
    q = deque([t1])
    w = d[t1][0]
    visit = (N + 1) * [False]
    visit[t1] = True
    check = False

    while q:
        cur = q.popleft()

        if cur == t2:
            check = True
            break

        for next_land, weight in d[cur]:
            if weight >= m:
                if not visit[next_land]:
                    visit[next_land] = True
                    q.append(next_land)

    if check:
        s = m + 1
        result = m
    else:
        e = m - 1

print(result)
