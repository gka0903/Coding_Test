def solution(s):
    stack = []  # 스택을 사용하여 반복 횟수와 문자열을 저장
    current_string = ""  # 현재 디코딩 중인 문자열
    current_num = 0  # 현재 반복 횟수를 저장할 변수

    for char in s:
        if char.isdigit():  # 숫자일 경우, 반복 횟수를 계산
            current_num = current_num * 10 + int(char)  # 여러 자리 숫자를 처리
        elif char == '[':  # '['가 나오면, 현재 상태를 스택에 저장
            stack.append((current_string, current_num))  # 현재 문자열과 반복 횟수 저장
            current_string = ""  # 새로운 문자열 시작
            current_num = 0  # 반복 횟수 초기화
        elif char == ']':  # ']'가 나오면, 스택에서 이전 상태를 가져옴
            last_string, num = stack.pop()  # 이전 문자열과 반복 횟수를 가져옴
            current_string = last_string + current_string * num  # 문자열 반복하여 합침
        else:
            current_string += char  # 일반 문자는 현재 문자열에 추가
        print(current_string, current_num)

    return current_string


print(solution("3[a2[c]]"))
