def floyd_warshall(graph):
    v = len(graph)

    dist = [row[:] for row in graph]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def solution(n, s, a, b, fares):
    INF = float('inf')

    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dist[i][i] = 0

    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f

    shortest_paths = floyd_warshall(dist)
    answer = shortest_paths[s][a] + shortest_paths[s][b]

    for k in range(1, n + 1):
        shortest_path = shortest_paths[s][k] + shortest_paths[k][b] + shortest_paths[k][a]
        answer = min(answer, shortest_path)

    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
