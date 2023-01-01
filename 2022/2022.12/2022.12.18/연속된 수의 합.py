def solution(num, total):
    answer = []
    for i in range(1000, -1000, -1):
        answer.append(i)
        if len(answer) > num:
            answer.pop(0)
        if sum(answer) == total and len(answer) == num:
            answer.sort()
            return answer


print(solution(5, 15))
