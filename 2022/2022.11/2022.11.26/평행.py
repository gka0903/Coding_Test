from itertools import combinations


def solution(dots):
    dot = list(combinations(dots, 2))
    stack = dots
    for i in dot:
        stack = dots
        stack.remove(i[0])
        stack.remove(i[1])
        print(stack)





print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
