from collections import deque


def solution(s):
    queue = deque(s)
    stack = []
    while queue:
        if stack:
            if stack[-1] == queue[0]:
                stack.pop()
                queue.popleft()
            else:
                stack.append(queue.popleft())
        else:
            stack.append(queue.popleft())

    if stack:
        return 0
    else:
        return 1




print(solution('baabaa'))
print(solution('cdcd'))
