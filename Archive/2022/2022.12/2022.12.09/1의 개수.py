def solution(n):
    if n % 2 == 0:
        return n + 1
    else:
        num = format(n, 'b')
        check = num.rfind('0')
        if check == -1:
            answer = '10' + num[1:]
        else:
            answer = num[:check] + '10' + num[check + 1:]
    return int(answer, 2)


print(solution(78))
print(solution(23))
