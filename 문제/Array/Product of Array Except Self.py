def solution(nums):
    # 0의 개수 구하기
    # 0의 개수별 풀이
    # 2개 일 때 다 0
    # 1개 일 때 하나만 빼고 다 0
    # 0개 모든 nums를 곱하고 answer 각 index에서 자기 위치만 나눠주기
    # zero_count = 0
    # mul = 1
    # for num in nums:
    #     if num == 0:
    #         zero_count += 1
    #
    # if zero_count >= 2:
    #     return [0] * len(nums)
    #
    # if zero_count == 1:
    #     answer = [0] * len(nums)
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             mul *= nums[i]
    #         else:
    #             zero_index = i
    #     answer[zero_index] = mul
    #     return answer
    #
    # if zero_count == 0:
    #     answer = []
    #     for num in nums:
    #         mul *= num
    #
    #     for num in nums:
    #         answer.append(mul // num)
    #     return answer

    n = len(nums)
    left = [1] * n
    right = [1] * n

    # Calculate left prefix product
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
        print("left", left)

    # Calculate right suffix product
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
        print("right", right)

    # Calculate result array
    result = [left[i] * right[i] for i in range(n)]

    return result


print(solution([1, 2, 3, 4]))
