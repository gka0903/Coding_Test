def findUnsortedSubarray(nums) -> int:
    dp = [True] * len(nums)
    result = 0
    first = -1
    second = -1
    for i in range(len(nums)):
        if i != 0:
            for j in range(i):
                if nums[i] < nums[j]:
                    dp[i] = False
                    break
        if i != len(nums) - 1:
            for j in range(len(nums) - 1, i, -1):
                if nums[i] > nums[j]:
                    dp[i] = False
                    break

    for f in range(len(dp)):
        if not dp[f]:
            first = f
            break
    for s in range(len(dp) - 1, -1, -1):
        if not dp[s]:
            second = s
            break
    if first == -1 and second - 1:
        return result
    result = second - first + 2

    return result


# 4 * O(n)풀이
# 그래프를 그려보기
# 그래프를 그렸을 때 시작점과 끝점을 찾는 방법을 알 수 있음
# 시작점은 꺾이는 지점의 가장 최솟값을 왼쪽으로(index가 더 작은 부분) 끌어와서 만나는 부분
# 끝점은 꺾이는 지점의 가장 최댓값을 오른쪽으로(index가 더 큰 부분) 끌어와서 만나는 부분
# 두 지점을 찾아서 길이 도출하면 정답

def solution(nums):
    # -100000 <= nums[i] <= 100000
    min_num = 100000
    max_num = -100000
    prev = nums[0]
    for i in range(len(nums)):
        if prev == nums[i]:
            pass
        if prev > nums[i]:
            min_num = min(min_num, nums[i])
        prev = nums[i]

    prev = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        if prev == nums[i]:
            pass
        if prev < nums[i]:
            max_num = max(max_num, nums[i])
        prev = nums[i]

    if min_num == 100000 or max_num == -100000:
        return 0
    
    for i in range(len(nums)):
        if nums[i] > min_num:
            point_one = i
            break
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < max_num:
            point_two = i
            break

    return point_two - point_one + 1


print("내 풀이: ", findUnsortedSubarray([1, 2, 3, 4]))
print("영상 보고 풀이: ", solution([1, 2, 3, 4]))
