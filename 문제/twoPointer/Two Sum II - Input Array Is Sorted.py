def solution(numbers, target):
    point_one = 0
    point_two = len(numbers) - 1

    while point_one <= point_two:
        sum_number = numbers[point_one] + numbers[point_two]
        if sum_number == target:
            return [point_one, point_two]
        elif sum_number > target:
            point_two -= 1
        else:
            point_one += 1
    return -1


print(solution([2, 7, 11, 15], 13))
