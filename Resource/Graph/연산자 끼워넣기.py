# 6
# 1 2 3 4 5 6
# 2 1 1 1

# import sys
#
# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
# op = list(map(int, sys.stdin.readline().split()))
# ops = ['+', '-', '*', '/']
# operators = []
#
# for i in range(4):
#     new_op = list(ops[i]) * op[i]
#     operators += new_op
#
# visit = [False] * len(operators)
# num_max, num_min = -1000000001, 10000000001
#
#
# def cal(p):
#     num = numbers[0]
#
#     for i in range(n - 1):
#         oper = p[i]
#
#         if oper == '+':
#             num += numbers[i + 1]
#         elif oper == '-':
#             num -= numbers[i + 1]
#         elif oper == '*':
#             num *= numbers[i + 1]
#         elif oper == '/':
#             if num < 0:
#                 num = ((num * -1) // numbers[i + 1]) * -1
#             else:
#                 num //= numbers[i + 1]
#     return num
#
#
# # dfs
# def dfs(p):
#     global num_max, num_min
#
#     if len(p) == n - 1:
#         num = cal(p)
#         if num > num_max:
#             num_max = num
#
#         if num < num_min:
#             num_min = num
#
#         return
#
#     for i in range(len(operators)):
#         if not visit[i]:
#             visit[i] = True
#             dfs(p + operators[i])
#             visit[i] = False
#
#
# dfs("")
#
# print(num_max)
# print(num_min)


import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

# 최댓값과 최솟값을 매우 작은/큰 수로 초기화
max_result = -1e9
min_result = 1e9


def dfs(index, current_result, add, sub, mul, div):
    global max_result, min_result

    # 종료 조건: 모든 숫자를 다 사용했을 때
    if index == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    # 재귀 호출: 각 연산자에 대해 가능한 경우 탐색
    if add > 0:
        dfs(index + 1, current_result + numbers[index], add - 1, sub, mul, div)
    if sub > 0:
        dfs(index + 1, current_result - numbers[index], add, sub - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * numbers[index], add, sub, mul - 1, div)
    if div > 0:
        # 문제의 나눗셈 조건(C++14 기준)을 파이썬으로 구현
        dfs(index + 1, int(current_result / numbers[index]), add, sub, mul, div - 1)


# DFS 시작
dfs(1, numbers[0], add, sub, mul, div)

print(max_result)
print(min_result)
