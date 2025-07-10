import heapq


def solution(n, works):
    answer = 0
    heap_works = [-x for x in works]
    heapq.heapify(heap_works)

    for i in range(n):
        work = -heapq.heappop(heap_works)

        if work == 0:
            break

        work -= 1
        heapq.heappush(heap_works, -work)

    for work in heap_works:
        answer += work ** 2

    return answer


print(solution(4, [1, 1]))
