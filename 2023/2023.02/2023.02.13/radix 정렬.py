from functools import reduce


def __flat(numbers):
    return reduce(lambda x, y: x + y, numbers)


def radix(numbers, num_digit):
    for digit in range(0, num_digit):
        arr_count = [[] for i in range(10)]
        for item in numbers:
            num = item // 10 ** digit % 10
            arr_count[num].append(item)
        numbers = __flat(arr_count)
    return numbers


def solution(numbers):
    num_digit = len(str(max(numbers)))
    A = radix(numbers, num_digit)
    return A


print(solution([3, 30, 34, 5, 9]))
