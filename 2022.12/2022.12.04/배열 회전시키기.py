from collections import deque



def solution(numbers, direction):
    answer = deque(numbers)
    if direction == "right":
        answer.rotate(1)
    else:
        answer.rotate(-1)

    return list(answer)



print(solution([1, 2, 3], "right"))
