def solution(nums):
    numbers = []
    for i in nums:
        k = int(str(i)[::-1])
        numbers.append(abs(i - k))
    count = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
    return count


print(solution([42, 11, 1, 97]))
