import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
visit = [False for _ in range(N + 1)]
start, end = map(int, input().split())
T = int(input())
conn = defaultdict(list)

for i in range(T):
    s, e = map(int, input().split())
    conn[s].append(e)
    conn[e].append(s)

result = float('INF')


def dfs(c, cnt, target):
    global result
    visit[c] = True

    if c == target:
        result = min(result, cnt)

    for n in conn[c]:
        if not visit[n]:
            dfs(n, cnt + 1, target)

    visit[c] = False


dfs(start, 0, end)

if result == float('INF'):
    print(-1)
else:
    print(result)
