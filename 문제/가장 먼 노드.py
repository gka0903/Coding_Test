import heapq


def solution(n, edge):
    answer = 0
    start = 1
    INF = float('inf')
    distances = {i: INF for i in range(1, n + 1)}
    connecting = {i: {} for i in range(1, n + 1)}

    for a, b in edge:
        connecting[a][b] = 1
        connecting[b][a] = 1

    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in connecting[current_node].items():
            distance = weight + current_distance

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    m = -1
    for v in distances.values():
        if m < v:
            m = v
            answer = 1
        elif m == v:
            answer += 1
            
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
