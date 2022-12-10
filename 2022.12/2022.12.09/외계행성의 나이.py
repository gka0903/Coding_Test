def solution(age):
    answer = ''
    ages = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = list(str(age))
    for i in age:
        answer += ages[int(i)]

    return answer


print(solution(23))
