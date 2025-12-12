import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
h = heapq
dict = defaultdict
MAX_SIZE = 10001
N, D = map(int, input().split())
d = dict(list)

for _ in range(N):
    s, e, w = map(int, input().split())
    d[s].append((e, w))

distance = [float("INF")] * MAX_SIZE
distance[0] = 0
q = []
h.heappush(q, (0, 0))

while q:
    cur_distance, cur_node = h.heappop(q)

    if distance[cur_node] < cur_distance:
        continue

    if cur_node == D:
        break

    if cur_node in d:
        for e, w in d[cur_node]:
            dist = w + cur_distance

            if dist < distance[e] and e <= D:
                distance[e] = dist
                h.heappush(q, (dist, e))

    dist = cur_distance + 1

    if cur_node + 1 <= D:
        if dist < distance[cur_node + 1]:
            distance[cur_node + 1] = dist
            h.heappush(q, (dist, cur_node + 1))

print(distance[D])
