from itertools import permutations


def checkNum(n):
    n = int(n)
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
    elif n == 2:
        return True
    else:
        return False
    return True


def solution(numbers):
    answer = 0
    ar = [int(i) for i in numbers]
    arr_check = []
    for i in range(len(ar) + 1):
        for j in list(permutations(ar, i)):
            number = '0'
            for num in j:
                number += str(num)
            number = int(number)
            if number not in arr_check:
                arr_check.append(number)
                if checkNum(number):
                    answer += 1
    return answer


print(solution("011"))
