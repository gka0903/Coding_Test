# dictionary를 통해 숫자들이 들어있는 계수를 value 값으로 넣고 value가 1인 값을 리턴
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


# hash table을 사용하여 이미 존재하면 존재하는 수를 지우는 것으로 하나 남은 값을 리턴
def solution2(nums):
    numbers = set()
    for i in range(len(nums)):
        if nums[i] not in numbers:
            numbers.add(nums[i])
        else:
            numbers.remove(nums[i])
    return numbers.pop()


# XOR 연산으로 같은 계산이 들어간 두번의 계산은 모두 사라짐
def solution3(nums):
    x = 0
    for num in nums:
        x ^= num
    return x


print(solution1([4, 1, 2, 1, 2]))
print(solution2([4, 1, 2, 1, 2]))
print(solution3([4, 1, 2, 1, 2]))
