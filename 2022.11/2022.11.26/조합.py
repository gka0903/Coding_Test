nums = [1, 2, 3, 4, 5]
answer_list = []


def nCr(n, ans, r):
    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return
    ans.append(nums[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)


nCr(0, [], 3)
print(answer_list)
