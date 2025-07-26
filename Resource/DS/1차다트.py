def solution(dartResult):
    numbers = []
    number = ""
    bonus = {'S', 'D', 'T'}
    options = {'*', '#'}
    for i in range(len(dartResult)):
        d = dartResult[i]

        if d in bonus or d in options:
            if number:
                numbers.append(int(number))
            number = ""
        else:
            number += d

    number_idx = -1

    for result in dartResult:
        if result in bonus:
            number_idx += 1

        if result == 'S':
            numbers[number_idx] **= 1
        elif result == 'D':
            numbers[number_idx] **= 2
        elif result == 'T':
            numbers[number_idx] **= 3

        if result == '#':
            numbers[number_idx] *= -1
        elif result == '*':
            numbers[number_idx] *= 2
            if number_idx > 0:
                numbers[number_idx - 1] *= 2

    return sum(numbers)


print(solution("1D2S0T"))
