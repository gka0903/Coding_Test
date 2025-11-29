from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    path = []
    stack = ["ICN"]

    # 그래프 가공
    for f, t in tickets:
        graph[f].append(t)

    # 그래프 속 리스트 정렬
    for k in graph.keys():
        graph[k].sort(reverse=True)

    # # dfs로 전체 탐색
    # def dfs(airport):
    #     while graph[airport]:
    #         top = graph[airport].pop()
    #         dfs(top)
    #
    #     path.append(airport)
    #
    # dfs("ICN")

    while stack:
        top = stack[-1]

        if not graph[top]:
            path.append(stack.pop())
        else:
            stack.append(graph[top].pop())

    return path[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
