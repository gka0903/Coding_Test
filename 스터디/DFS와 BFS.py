import collections
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
graph = collections.defaultdict(list)

N, M, start = map(int, input().split())

for i in range(M):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)

for i in graph:
    graph[i].sort()


def dfs(g, v, cur):
    v[cur] = True
    print(cur, end=" ")

    for i in g[cur]:
        if not v[i]:
            dfs(g, v, i)


def bfs(g, v, cur):
    q = collections.deque([cur])
    v[cur] = True

    while q:
        n = q.popleft()
        print(n, end=" ")
        for i in g[n]:
            if not v[i]:
                v[i] = True
                q.append(i)


visit = [False for _ in range(N + 1)]
dfs(graph, visit, start)
print()
visit = [False for _ in range(N + 1)]
bfs(graph, visit, start)
