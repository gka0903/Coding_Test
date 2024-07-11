def solution(nums, k):
    zero_que = []
    cur_length = 0
    max_length = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            cur_length += 1
        else:
            if k == 0:
                cur_length = 0
                continue
            if len(zero_que) < k:
                cur_length += 1
            else:
                cur_length = i - zero_que.pop(0)
            zero_que.append(i)
        if cur_length > max_length:
            max_length = cur_length

    return max_length


def longestOnes(nums, k: int) -> int:
    l = r = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        print(r, l, k)
    return r - l + 1


print(longestOnes([1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0], 2))
# print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
# print([0, 0, 1, 1, 1, 0, 0], 0)
