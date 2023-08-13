def lengthOfLastWord(s):
    string = s.split(" ")
    for i in range(len(string) - 1, -1, -1):
        print(string[i], i)
        if len(string[i]) != 0:
            return len(string[i])
    return 0


print(lengthOfLastWord("a"))
