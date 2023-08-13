def solution(M, N):
    answer = 0
    width = 0
    vertical = 0
    while M != 1:
        answer += 1
        width += 1
        M -= 1
    while N != 1:
        vertical += 1
        N -= 1
    answer += vertical * (width + 1)
    return answer


print(solution(2, 2))
print(solution(2, 5))

