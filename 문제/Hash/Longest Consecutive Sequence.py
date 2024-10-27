def solution(nums):
    hash_table = {}
    result = -1

    nums.sort()

    for i in nums:

        hash_table[i] = 1

        if i - 1 in hash_table:
            hash_table[i] += hash_table[i - 1]

    for i in hash_table:

        if result < hash_table[i]:
            result = hash_table[i]
    return result


print(solution([100, 4, 200, 1, 3, 2]))
