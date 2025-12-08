import heapq
import sys
from collections import defaultdict

h = heapq
input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = defaultdict(list)
graph_to_x = defaultdict(list)

for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph_to_x[B].append((A, C))

distance = {node: float("inf") for node in range(N + 1)}
distance[X] = 0
q = []
h.heappush(q, (distance[X], X))

while q:
    cur_dist, cur_node = h.heappop(q)

    if cur_dist > distance[cur_node]:
        continue

    for neighbor, weight in graph[cur_node]:
        dist = cur_dist + weight

        if dist < distance[neighbor]:
            distance[neighbor] = dist
            h.heappush(q, (dist, neighbor))

distance_to_x = {node: float("inf") for node in range(N + 1)}
distance_to_x[X] = 0
q_to_x = []
h.heappush(q_to_x, (distance_to_x[X], X))

while q_to_x:
    cur_dist, cur_node = h.heappop(q_to_x)

    if cur_dist > distance_to_x[cur_node]:
        continue

    for neighbor, weight in graph_to_x[cur_node]:
        dist = cur_dist + weight

        if dist < distance_to_x[neighbor]:
            distance_to_x[neighbor] = dist
            h.heappush(q_to_x, (dist, neighbor))

result = 0

for i in range(1, N + 1):
    d = distance[i] + distance_to_x[i]

    if d == float("inf"):
        continue

    if d > result:
        result = d

print(result)
