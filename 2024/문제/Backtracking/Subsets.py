def solution(nums):
    res = []
    stack = []

    def dfs(index):
        # 확인된 index가 기존 list 길이보다 길어지면 그 값을 받고 함수를 종료
        if index >= len(nums):
            res.append(stack.copy())
            return

        # 자기자신이 포함된 경우와 포함되지 않은 경우를 모두 체크
        dfs(index + 1)
        stack.append(nums[index])
        dfs(index + 1)
        stack.pop()

    dfs(0)

    return res


print(solution([1, 2, 3]))
