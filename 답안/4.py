from collections import deque


def solution(menu, order, k):
    answer = 0
    q = deque([order[0]])
    index = 1
    current_time = 0

    while q or index < len(order):
        o = q.popleft()
        current_time += menu[o]

        while index < len(order) and (current_time // k) + 1 >= index:
            q.append(order[index])
            index += 1

        answer = max(answer, len(q))
        print((current_time // k) + 1, index, q)
    return answer


print(solution([5, 12, 30], [1, 2, 0, 1], 10))
