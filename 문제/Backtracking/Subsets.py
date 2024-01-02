def solution(nums):
    res = []
    stack = []

    def backTracking(index):
        if index == len(nums):
            index -= 1
            return
        res.append(stack)
        stack.append(nums[index])
        backTracking(index + 1)
        stack.pop()

    backTracking(0)

    return res


print(solution([1, 2, 3]))
