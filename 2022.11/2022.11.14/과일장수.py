from collections import deque


def solution(k, m, score):
    result = 0
    queue = deque(sorted(score, reverse=True))


    while len(queue) >= m:
        stack = []
        for i in range(m):
            stack.append(queue.popleft())
        result += min(stack) * m

    return result


print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))