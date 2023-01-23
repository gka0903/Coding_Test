def solution(s):
    answer = []
    arr = ''
    for i in s:
        if i not in arr:
            arr += i
            answer.append(-1)
        else:
            num1 = arr.rfind(i)
            arr += i
            num2 = arr.rfind(i)
            answer.append(num2 - num1)

    return answer


print(solution("banana"))
