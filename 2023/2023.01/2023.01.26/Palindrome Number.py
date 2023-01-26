def isPalindrome(x):
    y = list(reversed(str(x)))
    return list(str(x)) == y


print(isPalindrome(121))
