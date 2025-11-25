import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

dic = defaultdict(list)
visit = [False] * (N + 1)

for i in range(M):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)


def dfs(n):
    visit[n] = True

    for next_n in dic[n]:
        if not visit[next_n]:
            dfs(next_n)


cnt = 0
for i in range(1, N + 1):
    if not visit[i]:
        cnt += 1
        dfs(i)

print(cnt)
