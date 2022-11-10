def isAnagram(s: str, t: str) -> bool:
    list_s = list(s)
    list_t = list(t)

    list_s.sort()
    list_t.sort()

    return list_s == list_t


print(isAnagram(s="anagram", t="nagaram"))
print(isAnagram(s = "rat", t = "car"))

