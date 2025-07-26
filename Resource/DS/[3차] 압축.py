def solution(msg):
    answer = []

    # 초기값 구성 ( a ~ z ) 사전, w, c
    alpha_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    d = {w: i + 1 for i, w in enumerate(alpha_list)}
    index = 26
    w = ""

    # 반복문
    for i in range(len(msg)):
        # w, c 값 초기화
        # 분기 index가 마지막 - c는 null
        w += msg[i]
        c = ""
        wc = ""
        if i + 1 != len(msg):
            c = msg[i + 1]

        # c == null w + c 확인 없음
        if c:
            wc = w + c

        # w == null 사전 추가 없음
        # w + c 사전에 없으면 추가
        # 있으면 continue
        if wc:
            if wc not in d:
                index += 1
                d[wc] = index
            else:
                continue

        # w 값 출력 후 초기화
        answer.append(d[w])
        w = ""

    return answer


print(solution("KAKAO"))
