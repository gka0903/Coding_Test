def solution(n, s):
    if s // n == 0:
        return [-1]

    answer = [s // n] * n
    answer_sum = sum(answer)

    if answer_sum != s:
        answer_remain = s % n

        for i in range(answer_remain):
            answer[-i - 1] += 1

    return answer


print(solution(3, 11))
