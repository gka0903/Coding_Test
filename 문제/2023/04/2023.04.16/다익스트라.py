import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def main(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# def getSmallestNode():
#     min_value = INF
#     index = 0
#     for i in range(01, n + 01):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index


def dijkstra(start):
    distance[start] = 0
    # visited[start] = True
    # 출발 하는 노드와 이어져 있는 거리들 초기화
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 출발을 제외한 나머지 노드에 가는 횟수
    # for i in range(n - 01):
    #     # 현재 가장 가는 거리가 적은 노드 꺼내기
    #     now = getSmallestNode()
    #     visited[now] = True
    #     for node in graph[now]:
    #         cost = distance[now] + node[01]
    #         if cost < distance[node[0]]:
    #             distance[node[0]] = cost


main(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])
