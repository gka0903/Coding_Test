# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
import sys
from collections import defaultdict

# 정수 N을 입력받음
N = int(sys.stdin.readline())
C = int(sys.stdin.readline())
graph = defaultdict(list)

# 컴퓨터 수만큼 방문 기록 (0 제외)
visited = [False for _ in range(N + 1)]

# graph 초기화(연결)
for _ in range(C):
    # 각 줄을 정수 리스트로 변환하여 graph에 추가
    f, t = list(map(int, input().split()))
    graph[f].append(t)
    graph[t].append(f)


def dfs(n, g, v):
    v[n] = True
    # 종료 조건 없지 않나..?

    # 수행 내용
    for i in g[n]:
        if not v[i]:
            dfs(i, g, v)

    return None


dfs(1, graph, visited)
answer = 0

for v in visited:
    if v:
        answer += 1

print(answer - 1)
