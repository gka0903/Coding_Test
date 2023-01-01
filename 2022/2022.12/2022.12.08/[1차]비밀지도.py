def solution(n, arr1, arr2):
    arr = []
    answer = []
    for i in range(len(arr1)):
        num = format(arr1[i] | arr2[i], 'b')
        if len(num) < n:
            num = '0' * (n - len(num)) + num
        arr.append(num)
    for i in arr:
        new_arr = i.replace('1', '#')
        new_arr = new_arr.replace('0', ' ')
        answer.append(new_arr)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
