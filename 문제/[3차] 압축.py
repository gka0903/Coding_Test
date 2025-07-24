def solution(msg):
    answer = []
    alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}

    w = ""
    c = ""
    index_number = 26
    len_msg = len(msg)

    for i in range(len_msg):
        w += msg[i]

        if i + 1 < len_msg:
            c = msg[i + 1]

        if c and w + c in alphabet_dict:
            continue

        if c:
            index_number += 1
            alphabet_dict[w + c] = index_number
        answer.append(alphabet_dict[w])
        w = ""
        c = ""

    return answer


print(solution("KAKAO"))
