from itertools import permutations


def solution(n):
    stack = []
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            stack.append(i)
            if i * i == n:
                answer += 1
    numbers = list(permutations(stack, 2))
    for num1, num2 in numbers:
        if num1 * num2 == n:
            answer += 1

    return answer


print(solution(100))
