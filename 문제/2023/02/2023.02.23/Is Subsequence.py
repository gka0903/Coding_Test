def isSubsequence(s, t):
    check_arr = list(s)
    for i in t:
        if check_arr[0] == i:
            check_arr.pop(0)
    if not check_arr:
        return True
    else:
        return False


print(isSubsequence("abc", "ahbgdc"))
