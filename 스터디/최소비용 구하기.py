import heapq
import sys

h = heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = dict([])

for i in range(M):
    A, B, C = map(int, input().split())

    if A not in graph:
        graph[A] = []

    graph[A].append((B, C))

start, end = map(int, input().split())
distance = {node: float("inf") for node in range(N + 1)}
distance[start] = 0
q = []
h.heappush(q, (distance[start], start))

while q:
    cur_distance, cur_node = h.heappop(q)

    if distance[cur_node] < cur_distance:
        continue

    if cur_node in graph:

        for neighbor, weight in graph[cur_node]:
            dist = weight + cur_distance

            if dist < distance[neighbor]:
                distance[neighbor] = dist
                h.heappush(q, (distance[neighbor], neighbor))

print(distance[end])
