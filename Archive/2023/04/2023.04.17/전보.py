import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    start, end, dis = map(int, input().split())
    graph[start].append((dis, end))
distance = [INF] * (n + 1)
q = []
heapq.heappush(q, (0, c))
distance[c] = 0
while q:
    dis, now = heapq.heappop(q)
    if distance[now] < dis:
        continue
    for i in graph[now]:
        cost = i[0] + dis
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

count = 0
for i in range(1, n + 1):
    if distance[i] == INF:
        distance[i] = 0
        continue
    elif c == i:
        continue
    else:
        count += 1
        m = max(m, distance[i])

print(count, m)
