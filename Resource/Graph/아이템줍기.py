from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 50이 최대 -> 2배해서 100이 최대
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]

    # 테두리 graph 만들기
    # 2배 해주기 겹쳐 있는 부분 삭제 위함
    for r in rectangle:
        x1, y1, x2, y2 = [x * 2 for x in r]

        # 각 사각형 돌면서 테두리 1
        # 안은 0
        for j in range(y1, y2 + 1):
            for i in range(x1, x2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[j][i] = 0
                elif graph[j][i] != 0:
                    graph[j][i] = 1

    # 캐릭터 위치랑 아이템 위치도 2배
    cX, cY, iX, iY = characterX * 2, characterY * 2, itemX * 2, itemY * 2

    # bfs로 최단 거리 찾기
    q = deque([(cX, cY)])
    d = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    while q:
        x, y = q.popleft()

        if x == iX and y == iY:
            answer = visited[y][x] // 2
            break

        for i in range(4):
            nx, ny = d[i][0] + x, d[i][1] + y

            if graph[ny][nx] == 1 and visited[ny][nx] == 1:
                visited[ny][nx] += visited[y][x]
                q.append([nx, ny])

    return answer


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
