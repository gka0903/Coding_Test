from collections import deque


def solution(priorities, location):
    answer = []
    answer_index = []
    queue = deque(priorities)
    index = deque(i for i in range(len(priorities)))
    while queue:
        biggest = True
        check = queue.popleft()
        for i in queue:
            if check < i:
                queue.append(check)
                index.append(index.popleft())
                biggest = False
                break
        if biggest:
            answer.append(check)
            answer_index.append(index.popleft())
    return answer_index.index(location) + 1



print(solution([1, 1, 9, 1, 1, 1], 0))
