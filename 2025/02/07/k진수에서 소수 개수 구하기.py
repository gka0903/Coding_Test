import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def to_n(n, k):
    result = ""

    while n > 0:
        r = n % k
        n //= k

        result = str(r) + result

    return result


def solution(n, k):
    numbers = to_n(n, k)
    checking = ""
    result = 0

    for num in numbers:
        if num == "0":
            if checking != "" and is_prime(int(checking)):
                result += 1

            checking = ""
        else:
            checking += num

    if checking and is_prime(int(checking)):
        result += 1
    return result


# print(solution(437674, 3))
print(solution(110011, 10))
