def solution(nums, k):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    d = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    result = []
    data = list(d.keys())
    for i in range(k):
        result.append(data[i])

    return result


print(solution([-1, -1], 1))
