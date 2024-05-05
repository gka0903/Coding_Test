def solution(chars):
    # char_index, check_index = 0, 0
    # while char_index < len(chars):
    #     check_index = char_index
    #     index = char_index
    #     while check_index < len(chars) and chars[check_index] == chars[char_index]:
    #         check_index += 1
    #
    #     count = check_index - char_index
    #
    #     if count > 1:
    #         for c in str(count):
    #             index += 1
    #             chars[index] = c
    #     chars = chars[:index + 1] + chars[check_index:]
    #     char_index = index + 1
    # return chars
    char_index, write_index = 0, 0

    while char_index < len(chars):
        current_char = chars[char_index]
        count = 0

        # 현재 문자가 계속 나타나는 동안 count를 증가
        while char_index < len(chars) and chars[char_index] == current_char:
            char_index += 1
            count += 1

        # 문자를 결과 위치에 저장
        chars[write_index] = current_char
        write_index += 1

        # count가 1보다 크면 숫자로 변환하여 배열에 저장
        if count > 1:
            count_str = str(count)
            for c in count_str:
                chars[write_index] = c
                write_index += 1
        print(chars)
    # 최종 길이 반환
    return write_index


print(solution(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
