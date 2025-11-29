# 입력
n, m = map(int, input().split())

# 그래프 초기화
# visit 초기화
graph = [i for i in range(1, n + 1)]
visit = [False] * len(graph)
paths = []


# dfs
def dfs(index, path):
    global paths

    # 종료 조건 len == m
    if len(path) == m:
        paths.append(path[:])
        return

    for i in range(n):
        if not visit[i]:
            path.append(graph[i])
            visit[i] = True
            dfs(i + 1, path)
            path.pop()
            visit[i] = False


dfs(0, [])

for path in paths:
    print(' '.join(map(str, path)))
