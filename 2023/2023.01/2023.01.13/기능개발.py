def solution(progresses, speeds):
    answer = []
    check = [False] * len(progresses)
    while check:
        stack = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                check[i] = True
            progresses[i] += speeds[i]
        if check[0]:
            while check and check[0]:
                stack += 1
                check.pop(0)
                progresses.pop(0)
                speeds.pop(0)
            answer.append(stack)
    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
