def solution(storey):
    answer = 0
    storey = str(storey)
    storey_len = len(storey)
    sep = 0

    for i in range(storey_len - 1, -1, -1):
        num = int(storey[i])
        if num > 5 or i != 0 and int(storey[i - 1]) >= 5 and num == 5:
            answer += 10 - num
            storey = int(storey)
            storey += (10 - num) * (10 ** sep)
            storey = str(storey)
            if storey_len != len(storey):
                sep += 1
                i -= 1
        else:
            answer += num
            storey = int(storey)
            storey -= num * (10 ** sep)
            storey = str(storey)
        sep += 1
    answer += int(storey) // 10 ** (len(storey) - 1)

    return answer


print(solution(95))
