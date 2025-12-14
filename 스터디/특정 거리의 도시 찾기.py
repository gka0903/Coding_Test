import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
h = heapq
g = defaultdict(list)
N, M, K, X = map(int, input().split())

for i in range(M):
    A, B = map(int, input().split())
    g[A].append(B)

q = []
h.heappush(q, (0, X))
distance = [float("inf") for _ in range(N + 1)]
distance[X] = 0

while q:
    cur_dist, cur_node = h.heappop(q)

    if distance[cur_node] < cur_dist:
        continue

    for node in g[cur_node]:
        dist = cur_dist + 1

        if dist < distance[node]:
            distance[node] = dist
            h.heappush(q, (dist, node))

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        check = True
        print(i)

if not check:
    print(-1)
