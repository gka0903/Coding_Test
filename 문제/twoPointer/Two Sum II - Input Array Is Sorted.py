def solution(numbers, target):
    point_one = 0
    point_two = len(numbers) - 1

    while point_one <= point_two:
        sum_number = numbers[point_one] + numbers[point_two]
        if sum_number == target:
            # 문제에서는 특이하게 인덱스 값에 하나를 더한 값들을 리턴하게 한다
            # 제출시에는 [point_one + 1, point_two + 1]로 제출하면 된다
            return [point_one, point_two]
        elif sum_number > target:
            point_two -= 1
        else:
            point_one += 1
    return -1


print(solution([2, 7, 11, 15], 13))
