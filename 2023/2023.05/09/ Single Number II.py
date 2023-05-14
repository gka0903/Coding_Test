def solution(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
            dic[i] += 1
    d = list(dict(sorted(dic.items(), key=lambda item: item[1])))
    return d[0]


print(solution([2, 2, 3, 2]))
