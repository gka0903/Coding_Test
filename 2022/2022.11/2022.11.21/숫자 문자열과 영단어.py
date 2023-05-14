def solution(s):
    stack = ''
    answer = ''
    for i in s:
        if ord(i) < ord('a'):
            answer += i

        else:
            stack += i

        if stack == 'zero':
            answer += '0'
            stack = ''
        elif stack == 'one':
            answer += '01'
            stack = ''
        elif stack == 'two':
            answer += '2'
            stack = ''
        elif stack == 'three':
            answer += '3'
            stack = ''
        elif stack == 'four':
            answer += '4'
            stack = ''
        elif stack == 'five':
            answer += '5'
            stack = ''
        elif stack == 'six':
            answer += '6'
            stack = ''
        elif stack == 'seven':
            answer += '7'
            stack = ''
        elif stack == 'eight':
            answer += '8'
            stack = ''
        elif stack == 'nine':
            answer += '9'
            stack = ''

    return int(answer)


print(solution("one4seveneight"))
