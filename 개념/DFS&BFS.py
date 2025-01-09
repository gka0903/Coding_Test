# 노드 개수 설정
from collections import deque

num_nodes = 6

# 빈 인접 리스트 생성
graph = [[] for _ in range(num_nodes)]


# 간선 추가 함수
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프일 경우


# 그래프에 간선 추가
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 3)
add_edge(graph, 1, 4)
add_edge(graph, 2, 5)
add_edge(graph, 4, 5)

visited = [False] * 6


# DFS
def dfs(graph, visited, index):
    visited[index] = True
    print(index, end=" ")

    for i in graph[index]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

            # dfs(graph, visited, 0)


bfs(graph, visited, 0)
