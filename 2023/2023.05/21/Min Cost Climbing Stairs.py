def solution(cost):
    dp_table = [0] * (len(cost) + 1)
    dp_table[0], dp_table[1] = cost[0], cost[1]
    for i in range(2, len(cost) + 1):
        if i == len(cost):
            c = 0
        else:
            c = cost[i]
        dp_table[i] = min(dp_table[i - 1] + c, dp_table[i - 2] + c)
    return dp_table[-1]


print(solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
