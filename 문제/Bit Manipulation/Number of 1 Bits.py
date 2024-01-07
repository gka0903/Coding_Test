# 마지막 자리가 1이면 1을 더하고
# 0이면 더하는게 없음
#  >> 연산자를 통해 비트를 왼쪽으로 하나씩 이동하면 값이 나옴
# Time Limit 걸림
def solution1(n):
    res = 0
    while n:
        res += n % 2
        n >> 1
    return res


# 마지막 자리 1이 있을 때는 그걸 제거하고 나머지는 똑같기 떄문에 & 쓰면 똑같이 유지
# 마지막이 0일경우 1이 있는 자리 1을 제거하고 그 뒤는 모두 1로 바뀜 -> 기존 값은 1이 있는 자리까지 모두
# 0이기 때문에 & 연산자로 계산되면 모두 0
def solutino2(n):
    res = 0
    while n:
        n &= (n - 1)
        res += 1
    return res


print(solution1(0b0000000000010000000))
