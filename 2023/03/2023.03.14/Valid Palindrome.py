def isPalindrome(s):
    if s == " ":
        return True
    c1, c2 = "", ""
    arr = s.split(',')
    for i in arr:
        a = [j for j in i if j.isalpha()]
        a = "".join(a).lower()
        print(a)
        if c1 != "" and c2 != "":
            if c1 == a[0] and c2 == a[-1]:
                continue
            else:
                return False
        else:
            c1, c2 = a[0], a[-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
