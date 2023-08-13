def solution(i, j, k):
    answer = 0
    for i in range(i, j + 1):
        arr = list(str(i))
        for j in arr:
            if j == str(k):
                answer += 1
    return answer


print(solution(1, 13, 1))
