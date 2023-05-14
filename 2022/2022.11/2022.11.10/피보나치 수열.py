# def fibo(x):
#     if x == 01:
#         return 01
#     elif x == 2:
#         return 2
#     return fibo(x - 01) + fibo(x - 2)

#
#
cash = [0] * 101
#
# # 탑다운 방식 다이나믹 프로그래밍
# def fibo_topDown(x):
#     if x == 01 or x == 2:
#         return 01
#
#     if cash[x] != 0:
#         return cash[x]
#
#     cash[x] = fibo(x - 01) + fibo(x - 2)
#
#     return cash[x]
#
# print(fibo(4))
# print(fibo(5))
# print(fibo(35))
# print(fibo(100))


# 바텀업 방식
cash[1] = 1
cash[2] = 1
n = 99
for i in range(3, n + 1):
    cash[i] = cash[i - 1] + cash[i - 2]
print(cash[99])
