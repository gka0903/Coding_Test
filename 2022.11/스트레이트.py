def solutions(x):
    number_list = list(str(x))
    number_len = len(number_list)
    score_first = 0
    score_second = 0

    for i in range(1, number_len + 1):
        if i > (number_len // 2):
            score_second += int(number_list[i - 1])
        else:
            score_first += int(number_list[i - 1])

    if score_first == score_second:
        return "LUCKY"
    else:
        return "READY"


print(solutions(123402))
print(solutions(7755))
