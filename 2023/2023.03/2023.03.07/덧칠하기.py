# def solution(n, m, section):
#     answer = 0
#     block = [1] * n
#     for i in section:
#         block[i - 1] = 0
#     for number in range(n):
#         if block[number] == 0:
#             for j in range(m):
#                 if number + j >= n:
#                     break
#                 block[number + j] = 1
#             answer += 1
#     return answer


def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer


print(solution(4, 1, [1, 2, 3, 4]))
