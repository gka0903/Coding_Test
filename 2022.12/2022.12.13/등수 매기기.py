def solution(score):
    nums = []
    answer = []
    for i in score:
        nums.append(sum(i))
    arr = sorted(nums, reverse=True)
    check = []
    for _ in arr:
        if _ not in check:
            check.append(_)
        else:
            check.append("*")

    for i in nums:
        answer.append(check.index(i) + 1)
    return answer





print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
