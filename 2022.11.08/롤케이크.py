# 시간오류
def solution(topping):
    result = 0
    for i in range(1, len(topping) - 1):
        first_stack = []
        first_result = 0
        second_stack = []
        second_result = 0
        for j in range(i):
            if topping[j] not in first_stack:
                first_stack.append(topping[j])
                first_result += 1
        for z in range(i, len(topping)):
            if topping[z] not in second_stack:
                second_stack.append(topping[z])
                second_result += 1
        if first_result == second_result:
            result += 1

    return result


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
