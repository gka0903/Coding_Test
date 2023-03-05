def singleNonDuplicate(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
        elif arr[0] != i:
            return arr[0]
        else:
            arr = []


print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
