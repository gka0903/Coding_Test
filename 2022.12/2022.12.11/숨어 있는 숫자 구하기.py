import re


def solution(my_string):
    numbers = list(map(int, re.findall(r'\d+', my_string)))
    return sum(numbers)



print(solution("aAb1B2cC34oOp"))
