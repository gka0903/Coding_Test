def solution(num, k):
    num = str(num)
    answer = num.find(str(k))
    if answer != -1:
        answer += 1
    return answer


print(solution(29183, 1))
print(solution(123456, 7))