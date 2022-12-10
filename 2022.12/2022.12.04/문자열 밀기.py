def solution(A, B):
    stack = []
    answer = 0
    for i in A:
        stack.append(i)
    for _ in stack:
        if "".join(stack) == B:
            return answer
        word = stack.pop()
        stack.insert(0, word)
        answer += 1
    return -1




print(solution("hello", "ohell"))
