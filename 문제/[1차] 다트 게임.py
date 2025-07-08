import re


def solution(dartResult):
    # 1. 정규표현식으로 점수-보너스-옵션 분리
    pattern = re.compile(r'(\d{1,2})([SDT])([*#]?)')
    parsed = pattern.findall(dartResult)

    scores = []

    for i, (num, bonus, option) in enumerate(parsed):
        num = int(num)
        if bonus == 'S':
            num = num ** 1
        elif bonus == 'D':
            num = num ** 2
        elif bonus == 'T':
            num = num ** 3

        if option == '*':
            num *= 2
            if i > 0:
                scores[i - 1] *= 2  # 이전 점수도 2배
        elif option == '#':
            num *= -1

        scores.append(num)

    return sum(scores)
