import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
h = heapq
graph = defaultdict(list)
N, E = map(int, input().split())


for i in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

v1, v2 = map(int, input().split())


def shortest_(start, end):
    distance = [float("inf")] * (N + 1)
    distance[start] = 0
    q = []
    h.heappush(q, (distance[start], start))

    while q:
        cur_dist, node = h.heappop(q)

        if distance[node] < cur_dist:
            continue

        for next_node, weight in graph[node]:
            dist = cur_dist + weight

            if dist < distance[next_node]:
                distance[next_node] = dist
                h.heappush(q, (dist, next_node))

    return distance[end]


# 경로 1 s -> v1 -> v2 -> e
# 경로 2 s -> v2 -> v1 -> e
v1_first = shortest_(1, v1) + shortest_(v1, v2) + shortest_(v2, N)
v2_first = shortest_(1, v2) + shortest_(v2, v1) + shortest_(v1, N)
result = min(v2_first, v1_first)

if result != float("inf"):
    print(result)
else:
    print(-1)
