from collections import defaultdict


def solution(tickets):
    # 1. 그래프 생성 및 정렬
    # 각 공항을 key로, 도착 공항 리스트를 value로 갖는 그래프를 만듭니다.
    graph = defaultdict(list)

    # 도착지를 알파벳 역순으로 정렬합니다.
    # 이렇게 하면 pop()을 사용했을 때 알파벳 순서가 가장 빠른 공항이 나옵니다.
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)

    # 2. DFS 탐색 시작
    path = []
    # 탐색 경로를 담을 스택. 시작은 항상 "ICN"
    stack = ["ICN"]

    while stack:
        # 스택의 가장 위에 있는 공항(현재 위치)을 확인만 합니다. (꺼내지 않음)
        current = stack[-1]

        # 1) 현재 공항에서 출발하는 항공권이 없거나, 이미 다 사용한 경우
        if not graph[current]:
            # 더 이상 갈 곳이 없으므로, 이 공항을 최종 경로(path)에 추가하고 스택에서 제거
            path.append(stack.pop())
        # 2) 아직 사용할 수 있는 항공권이 있는 경우
        else:
            # 알파벳 순으로 가장 앞서는 목적지를 스택에 추가
            stack.append(graph[current].pop())

    # 3. 결과 반환
    # path가 역순으로 만들어졌으므로, 다시 뒤집어서 반환합니다.
    return path[::-1]


def solution2(tickets):
    # 1. 그래프 생성 및 목적지 정렬
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # 재귀적으로 탐색할 때 알파벳 순서가 빠른 곳부터 방문하기 위해 오름차순 정렬
    for key in graph:
        graph[key].sort()

    # 최종 경로를 담을 변수
    path = []

    # 2. DFS 재귀 함수 정의
    def dfs(current):
        # 현재 공항에서 갈 수 있는 목적지들을 순회
        while graph[current]:
            # 알파벳 순으로 가장 빠른 목적지를 꺼내서 "사용" 처리
            next_dest = graph[current].pop(0)
            # 해당 목적지로 더 깊이 탐색
            dfs(next_dest)

        # 더 이상 갈 곳이 없을 때(막다른 길에 도달했을 때), 경로에 추가
        path.append(current)

    # 3. 탐색 시작
    dfs("ICN")

    # 4. 결과 반환
    # path는 역순으로 쌓이므로 뒤집어서 반환
    return path[::-1]


## 1. 최단 경로 찾기 (BFS)

# "A에서 B로 가는 가장 짧은 이야기"
# BFS는 큐(Queue)를 사용하여 시작점에서 가까운 순서대로 탐색합니다. 경로를 추적하기 위해 큐에 다음 노드뿐만 아니라, 현재까지의 경로 전체를 넣습니다.
from collections import deque


def find_shortest_path(graph, start, end):
    """BFS를 이용해 최단 경로를 찾습니다."""
    # 큐에는 앞으로 탐색할 경로들을 저장합니다. 시작은 [start] 경로 하나입니다.
    queue = deque([[start]])
    visited = {start}

    while queue:
        # 큐에서 가장 오래된 경로를 꺼냅니다.
        path = queue.popleft()
        current_node = path[-1]

        # 목적지에 도착했다면, 이 경로가 최단 경로입니다.
        if current_node == end:
            return path

        # 현재 노드에서 갈 수 있는 이웃 노드들을 탐색합니다.
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # 기존 경로에 이웃 노드를 추가하여 새로운 경로를 만듭니다.
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  # 경로가 없는 경우


## 2. 경로 존재 여부 확인 (DFS)
# "A에서 B로 가는 이야기가 있긴 한지 확인"
# DFS는 재귀를 이용해 한 경로를 깊게 파고듭니다. 경로를 발견하는 즉시 탐색을 멈추고 해당 경로를 반환합니다.

def find_a_path(graph, start, end):
    """DFS를 이용해 존재하는 경로 하나를 찾습니다."""
    visited = set()

    def dfs(current, path):
        # 현재 노드를 방문 처리하고 경로에 추가합니다.
        visited.add(current)
        path.append(current)

        # 목적지에 도착했다면, 완성된 경로를 반환합니다.
        if current == end:
            return path

        # 이웃 노드들을 깊이 우선으로 탐색합니다.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                # 재귀 호출에서 경로를 찾았다면, 그 경로를 계속 반환하여 탐색을 종료합니다.
                result_path = dfs(neighbor, path)
                if result_path:
                    return result_path

        # 이 분기에서는 경로를 찾지 못했으므로 경로에서 현재 노드를 제거합니다(백트래킹).
        path.pop()
        return None

    # 탐색 시작
    return dfs(start, [])


# 모든 경로
def find_all_paths(graph, start, end):
    """DFS와 백트래킹을 이용해 모든 경로를 찾습니다."""
    all_paths = []

    def dfs(current, path):
        # 현재 노드를 경로에 추가합니다.
        path.append(current)

        # 목적지에 도착했다면, 현재까지의 경로를 복사해서 결과 리스트에 추가합니다.
        # 여기서 탐색을 멈추지 않습니다.
        if current == end:
            all_paths.append(list(path))  # ★★★ 중요: 경로를 복사해서 추가

        # 이웃 노드들을 계속 탐색합니다.
        for neighbor in graph.get(current, []):
            dfs(neighbor, path)

        # ★★★ 백트래킹 ★★★
        # 현재 노드에서 출발하는 모든 탐색이 끝났으므로,
        # 이전 노드로 돌아가 다른 경로를 탐색할 수 있도록 현재 노드를 경로에서 제거합니다.
        path.pop()

    # 탐색 시작
    dfs(start, [])
    return all_paths
