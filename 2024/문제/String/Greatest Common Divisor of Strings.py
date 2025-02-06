def solution(str1, str2):
    # 길이 더 작은 거 만큼 반복
    # str2 로 str1 나눠지면 리턴
    # 다음 반복 실행 길이 하나 적게해서("ABC" -> "AB")
    sh = str1 if len(str1) < len(str2) else str2

    for i in range(len(sh)):
        t = sh
        s1 = str1
        while len(s1) >= len(t):
            if s1[0:len(t)] == t:
                s1 = s1[len(t):]
            else:
                break
        s2 = str2
        while len(s2) >= len(t):
            if s2[0:len(t)] == t:
                s2 = s2[len(t):]
            else:
                break
        if s1 == "" and s2 == "":
            return t
        print(i, t, s1, s2)
        sh = t[:-1]
    return ""


def youtubeEdition(str1, str2):
    len1, len2 = len(str1), len(str2)

    def isDivisor(l):
        if len1 % l or len2 % l:
            return False
        f1, f2 = len1 // l, len2 // l
        return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

    for l in range(min(len1, len2), 0, -1):
        if isDivisor(l):
            return str1[:l]
    return ""


print(youtubeEdition("ABABAB", "ABAB"))
