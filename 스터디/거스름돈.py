import sys

input = sys.stdin.readline
N = int(input())
dp = [float("inf")] * (N + 1)
dp[0] = 0


for i in range(2, N + 1):
    if i >= 2:
        dp[i] = dp[i - 2] + 1
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[N] != float("inf"):
    print(dp[N])
else:
    print(-1)


import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제 (필수)
input = sys.stdin.readline

N = int(input())
INF = float("inf")

# 1. 메모이제이션 테이블 (-1로 초기화: 아직 방문 안 함)
memo = [-1] * (N + 1)


def recursive_solve(n):
    # [기저 조건 1] 성공: 0원을 만드는 데는 동전 0개가 필요함
    if n == 0:
        return 0

    # [기저 조건 2] 실패: 음수가 되면 불가능한 경로임 (무한대 리턴)
    if n < 0:
        return INF

    # [메모이제이션] 이미 계산한 적이 있다면 그 값 리턴
    if memo[n] != -1:
        return memo[n]

    # [점화식] 2원을 썼을 때 vs 5원을 썼을 때 중 작은 값 선택
    # 1을 더하는 이유는 동전 하나를 썼기 때문
    memo[n] = min(recursive_solve(n - 2), recursive_solve(n - 5)) + 1

    return memo[n]


# 실행
result = recursive_solve(N)

# 결과 출력 (INF보다 크거나 같으면 못 만든다는 뜻)
if result >= INF:
    print(-1)
else:
    print(result)
