from collections import Counter


def solution(str1, str2):
    str_1 = []
    str_2 = []

    for i in range(len(str1) - 1):
        word = ""

        for w in str1[i:i + 2]:
            if not w.isalpha():
                continue

            word += w.upper()

        if len(word) == 2:
            str_1.append(word)

    for i in range(len(str2) - 1):
        word = ""

        for w in str2[i:i + 2]:
            if not w.isalpha():
                continue

            word += w.upper()

        if len(word) == 2:
            str_2.append(word)

    set_str1 = Counter(str_1)
    set_str2 = Counter(str_2)

    intersection = set_str1 & set_str2
    union = set_str1 | set_str2

    a = 0
    b = 0
    for i in intersection:
        a += intersection[i]

    for i in union:
        b += union[i]

    return int(a / b * 65536) if b != 0 else 1


print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))

# str1 = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
