import heapq
import sys

input = sys.stdin.readline
h = heapq
K, N = map(int, input().split())

MAX_SIZE = 100001
distance = [float("inf")] * MAX_SIZE
distance[K] = 0
q = []
h.heappush(q, (distance[K], K))

while q:
    cur_distance, cur_node = h.heappop(q)

    if distance[cur_node] < cur_distance:
        continue

    if cur_node == N:
        break

    for next_node in [cur_node - 1, cur_node + 1]:
        if 0 <= next_node < MAX_SIZE:
            dist = cur_distance + 1

            if distance[next_node] > dist:
                distance[next_node] = dist
                h.heappush(q, (distance[next_node], next_node))

    if 0 <= cur_node * 2 < MAX_SIZE:
        if distance[cur_node * 2] > cur_distance:
            distance[cur_node * 2] = cur_distance
            h.heappush(q, (distance[cur_node * 2], cur_node * 2))

print(distance[N])
