def solution(n):
    res = []
    stack = []

    def rec(left, right):
        if n == left == right:
            res.append("".join(stack))
            return
        if left < n:
            stack.append("(")
            rec(left + 1, right)
            stack.pop()
        if right < left:
            stack.append(")")
            rec(left, right + 1)
            stack.pop()

    rec(0, 0)
    return res


print(solution(1))
