import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)
result = 0
dis = 0
distance.sort()
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력\
    if distance[i] == INF:
        continue
    else:
        if dis < distance[i]:
            result += 1
            dis = distance[i]

print(result, dis)
