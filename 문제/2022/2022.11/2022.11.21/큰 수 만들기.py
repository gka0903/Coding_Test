def solution(number, k):
    number = list(number)
    index = 0
    while True:
        if number[index] < number[index + 1]:
            number.pop(index)
            index = 0
            k -= 1
        else:
            index += 1
        if k == 0:
            break

    answer = ''.join(number)
    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
