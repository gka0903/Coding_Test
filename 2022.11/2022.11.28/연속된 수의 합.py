def solution(num, total):
    for i in range(total, -10, -1):
        answer = []
        for j in range(num):
            answer.append(i - j)
        if sum(answer) == total:
            answer.sort()
            return answer


print(solution(2, 15))
