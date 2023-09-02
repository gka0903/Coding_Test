def solution(nums, k):
    nums.sort()
    result = []
    count = 0
    check = len(nums)
    if len(nums) % k != 0:
        return False
    while nums:
        print(nums, count)
        for i in nums:
            if i not in result:
                if not result:
                    result.append(i)
                    nums.remove(i)
                else:
                    if result[-1] + 1 == i:
                        result.append(i)
                        nums.remove(i)
                    else:
                        continue
            if len(result) == k:
                result = []
                count = 0
                break
        count += 1
        if count == check:
            return False
    return nums == []


print(solution([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
