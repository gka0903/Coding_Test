from collections import Counter


def singleNumber(nums):
    num = Counter(nums).most_common()[-1]
    return num[0]


print(singleNumber([2, 2, 1]))
