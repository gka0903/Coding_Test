import heapq
import sys
from collections import defaultdict

h = heapq
input = sys.stdin.readline
V, E = map(int, input().split())
s = int(input())
graph = defaultdict(list)

# 그래프
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 초기화
distance = [float("INF")] * (V + 1)
distance[s] = 0
q = []
h.heappush(q, (distance[s], s))

while q:
    # 출력
    cur_d, cur_n = h.heappop(q)

    if distance[cur_n] < cur_d:
        continue

    # 갱신
    for node, weight in graph[cur_n]:
        dis = cur_d + weight

        if dis < distance[node]:
            distance[node] = dis
            h.heappush(q, (distance[node], node))

for i in range(1, len(distance)):
    if distance[i] == float("inf"):
        print("INF")
    else:
        print(distance[i])
