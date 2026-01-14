import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([(X, 0)])
visit = [False] * (N + 1)
visit[X] = True
check = False
result = []

while q:
    cur_graph, dist = q.popleft()

    if dist == K:
        result.append(cur_graph)
        check = True

    for g in graph[cur_graph]:
        if not visit[g]:
            visit[g] = True
            q.append((g, dist + 1))

if not check:
    print(-1)
else:
    result.sort()
    for g in result:
        print(g)
