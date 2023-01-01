def solution(polynomial):
    arr_x = []
    answer = ''
    num, num_x = 0, 0
    polynomial = polynomial.split()
    for i in polynomial:
        if 'x' in i:
            arr_x.append(i)
        if i.isdigit():
            num += int(i)
    for i in arr_x:
        if i == 'x':
            num_x += 1
        else:
            num_x += int(i[:len(i) - 1])

    if num_x == 0 and num != 0:
        answer = str(num)
    elif num_x != 0 and num == 0:
        if num_x == 1:
            return 'x'
        answer = str(num_x) + 'x'
    else:
        answer = str(num_x) + 'x + ' + str(num)
        if num_x == 1:
            answer = 'x' + ' + ' + str(num)

    return answer




print(solution("3x + 7 + x"))
