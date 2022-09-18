def solution(s):
    answer = True

    for i in s:
        if ord(i) >= ord('A'):
            answer = False
    if len(s) not in [4, 6]:
        answer = False
        
    return answer

print(solution("12341234"))