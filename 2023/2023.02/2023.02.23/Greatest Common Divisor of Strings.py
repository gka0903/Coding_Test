def gcdOfStrings(str1, str2):
    if len(str1) < len(str2):
        m_len = len(str1)
    else:
        m_len = len(str2)
    string = ''
    check_string = ''
    for i in range(m_len):
        if str1[i] == str2[i]:
            check_string += str1[i]
        l_check = len(check_string)
        for s1 in range(len(str1) // l_check):
            if str1[s1:s1 + s1] != check_string:
                break
                return ''
            else:
                continue
        for s2 in range(len(str2) // l_check):
            if str2[s2:s2 + s2] != check_string:
                break
                return ''
            else:
                continue


print(gcdOfStrings("ABCABC", "ABC"))
