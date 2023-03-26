def isPalindrome(s):
    string = "".join([j for j in s if j.isalnum()])
    string = string.lower()

    if string == string[::-1]:
        return True
    else:
        return False


print(isPalindrome("0P"))
