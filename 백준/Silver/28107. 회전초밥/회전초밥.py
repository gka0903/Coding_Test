import sys
from collections import defaultdict, deque

input = sys.stdin.readline
d = defaultdict(deque)
N, M = map(int, input().split())
c = [0] * (N + 1)

for i in range(1, N + 1):
    li = list(map(int, input().split()))[1:]

    for l in li:
        d[l].append(i)

dish = list(map(int, input().split()))

for fish in dish:
    if d[fish]:
        person = d[fish].popleft()
        c[person] += 1

print(*c[1:])
