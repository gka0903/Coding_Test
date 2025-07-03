import heapq


def solution(operations):
    heap_max = []
    heap_min = []
    heap_ = set()

    for operation in operations:
        op, number = operation.split(" ")
        n = int(number)

        if op == "I":
            heap_.add(n)
            heapq.heappush(heap_max, -n)
            heapq.heappush(heap_min, n)
        else:
            if not heap_:
                continue

            if number == "1":
                while heap_max:
                    max_number = -heapq.heappop(heap_max)

                    if max_number in heap_:
                        heap_.remove(max_number)
                        break
            elif number == "-1":
                while heap_min:
                    min_number = heapq.heappop(heap_min)

                    if min_number in heap_:
                        heap_.remove(min_number)
                        break

    if heap_:
        max_n = max(heap_)
        min_n = min(heap_)

        return [max_n, min_n]

    return [0, 0]


# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
