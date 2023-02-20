def findWords(words):
    L1 = 'qwertyuiop'
    L2 = 'asdfghjkl'
    L3 = 'zxcvbnm'
    arr = []
    for i in words:
        lower_word = i.lower()
        check = ''
        for j in lower_word:
            if j in L1:
                check += '1'
            elif j in L2:
                check += '2'
            else:
                check += '3'
        c = check[0]
        num_check = True
        for num in range(1, len(check)):
            if check[num] != c:
                num_check = False
        if num_check:
            arr.append(i)
    return arr


print(findWords(["Adsdf", "sfd"]))
