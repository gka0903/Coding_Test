def searchMatrix(matrix, target):
    target_i = []
    for i in matrix:
        if i[-1] < target:
            continue
        elif i[-1] > target:
            target_i = i
            break
        else:
            return True
    if not target_i:
        return False
    low = 0
    height = len(target_i) - 1
    while low <= height:
        mid = (low + height) // 2
        if target_i[mid] == target:
            return True
        elif target_i[mid] > target:
            height = mid - 1
        else:
            low = mid + 1
    return False


print(searchMatrix([[1]], 0))
