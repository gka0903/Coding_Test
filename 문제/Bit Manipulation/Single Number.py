def solution1(nums):
    numbers = {}
    for i in range(len(nums)):
        if nums[i] not in numbers:
            numbers[nums[i]] = 1
        else:
            numbers[nums[i]] += 1
    for key, val in numbers.items():
        if val == 1:
            return key


def solution2(nums):
    numbers = set()
    for i in range(len(nums)):
        if nums[i] not in numbers:
            numbers.add(nums[i])
        else:
            numbers.remove(nums[i])
    return numbers.pop()


def solution3(nums):
    x = 0
    for num in nums:
        x ^= num
    return x


print(solution1([4, 1, 2, 1, 2]))
print(solution2([4, 1, 2, 1, 2]))
print(solution3([4, 1, 2, 1, 2]))
