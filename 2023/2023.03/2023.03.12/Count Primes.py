def checkPrimeNum(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True


def countPrimes(n):
    answer = 0
    if n <= 2:
        return 0
    for i in range(2, n):
        if checkPrimeNum(i):
            answer += 1
    return answer


print(countPrimes(10))
