def change_n(n, number):
    digit = "0123456789ABCDEF"
    result = ""
    if number == 0:
        return "0"
    while number > 0:
        result = digit[number % n] + result
        number //= n
    return result


def solution(n, t, m, p):
    answer = ''
    number = 0
    turn = 1

    while len(answer) < t:
        changed_number = change_n(n, number)

        for num in changed_number:
            if (turn - 1) % m + 1 == p:
                if len(answer) < t:
                    answer += num

            turn += 1

        number += 1

    return answer


# print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
