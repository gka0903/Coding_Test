def solution(arr):
    prefix_sum = []
    s = 0
    for i in arr:
        s += i
        prefix_sum.append(s)

    return prefix_sum[len(arr) - 1]


print(solution([10, 20, 30, 40, 50]))
