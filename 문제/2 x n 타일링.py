def solution(n):
    NUM = 1_000_000_007

    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = {1: 1, 2: 2}

    for i in range(3, n + 1):
        if i in dp:
            continue

        dp[i] = (dp[i - 2] % NUM + dp[i - 1] % NUM) % NUM

    return dp[n]


def solution2(n):
    NUM = 1_000_000_007
    a = 1
    b = 2

    for i in range(3, n + 1):
        temp = b
        b = (a + b) % NUM
        a = temp % NUM

    return b


print(solution(4))
