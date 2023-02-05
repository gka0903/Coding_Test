def solution(s, skip, index):
    answer = ''
    skip = list(map(ord, skip))
    for i in s:
        word = ord(i)
        for _ in range(index):
            word += 1
            if word > ord('z'):
                word = ord('a')
            while word in skip:
                word += 1
                if word > ord('z'):
                    word = ord('a')
        answer += chr(word)

    return answer


print(solution("z", "abcdefghij", 20))
