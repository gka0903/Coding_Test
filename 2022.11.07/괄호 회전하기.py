from collections import deque


def solution(s):
    queue = deque(s)
    answer = 0

    for i in range(len(s)):
        if i != 0:
            drop_word = queue.popleft()
            queue.append(drop_word)

        stack = []
        for q in queue:
            if not stack:
                stack.append(q)
            else:
                if "(" in stack and q == ")":
                    stack.pop()
                elif "[" in stack and q == "]":
                    stack.pop()
                elif '{' in stack and q == "}":
                    stack.pop()
                else:
                    stack.append(q)

        if not stack:
            answer += 1


    return answer


print(solution("[](){}"))
