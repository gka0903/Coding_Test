arr = ['1', '2', '4']


def recursive(result, n):
    result = arr[n % 3] + result
    if n // 3 == 0:
        return result
    return recursive(result, n // 3 - 1)


def solution(n):
    n -= 1
    answer = recursive('', n)

    return str(answer)


print(solution(10))
