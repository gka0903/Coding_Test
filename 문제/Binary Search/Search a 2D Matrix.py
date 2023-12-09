def solution(matrix, target):
    target_list = matrix[len(matrix) - 1]
    for i in range(len(matrix)):
        if target < matrix[i][0]:
            target_list = matrix[i - 1]
            break
        elif target == matrix[i][0]:
            target_list = matrix[i]
            break
            
    first_point = 0
    end_point = len(target_list) - 1
    while first_point <= end_point:
        mid = (first_point + end_point) // 2
        if target_list[mid] == target:
            return True
        elif target_list[mid] > target:
            end_point = mid - 1
        else:
            first_point = mid + 1

    return False


print(solution([[1], [3]], 3))
