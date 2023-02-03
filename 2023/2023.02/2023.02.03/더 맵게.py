import heapq


def solution(scoville, K):
    h = []
    count = 0
    for i in scoville:
        heapq.heappush(h, i)
    while h[0] < K:
        if len(h) == 1:
            return -1
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        c = a + 2 * b
        heapq.heappush(h, c)
        count += 1
    return h, count


print(solution([1, 2, 3, 9, 10, 12], 7))
