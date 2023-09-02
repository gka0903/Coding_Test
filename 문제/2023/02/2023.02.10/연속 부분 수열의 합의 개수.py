def solution(elements):
    arr = elements * 2
    check_arr = {sum(elements)}
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            num = sum(arr[j:i + j])
            if num not in check_arr:
                check_arr.add(num)
    return len(check_arr)


print(solution([7, 9, 1, 1, 4]))
