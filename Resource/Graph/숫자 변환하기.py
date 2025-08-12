from collections import deque


def cal(current, n):
    c = set()

    for i in current:
        c.add(i + n)
        c.add(i * 2)
        c.add(i * 3)
    return c


def solution(x, y, n):
    answer = 0
    queue = deque([{x}])

    if x == y:
        return 0

    while queue:
        answer += 1
        current = queue.popleft()
        cal_list = cal(current, n)

        if y in cal_list:
            return answer

        if min(cal_list) > y:
            return -1

        queue.append(cal_list)

    return answer


print(solution(2, 5, 4))
