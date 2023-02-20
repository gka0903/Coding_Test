def runningSum(nums):
    s = 0
    arr = []
    for i in nums:
        s += i
        arr.append(s)
    return arr


print(runningSum([1, 2, 3, 4]))
