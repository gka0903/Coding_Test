def solution(m, n, puddles):
    answer = 0
    MOD = 1_000_000_007

    # dp 테이블(지도) 만들고
    dp = [[0] * m for _ in range(n)]
    p = set()

    # puddles set 만들고
    for x, y in puddles:
        p.add((x - 1, y - 1))

    dp[0][0] = 1

    # 지도 돌면서 puddles 확인 하면서 연산
    # 연산은 올 수 있는 길(왼쪽, 위쪽) 두가지를 합해서 올 수 있는 경우의 수 전체 계산
    for y in range(n):
        for x in range(m):
            if x == 0 and y == 0:
                continue

            # 웅덩이 스킵
            if (x, y) in p:
                continue

            way = 0
            if x - 1 >= 0:
                way += dp[y][x - 1]

            if y - 1 >= 0:
                way += dp[y - 1][x]

            dp[y][x] = way % MOD

    return dp[-1][-1]


print(solution(4, 3, [[2, 2]]))
