def solution(s):
    vowels = "aeiou"
    indexes_vowels = []
    for i in range(len(s)):
        if s[i] in vowels or s[i] in vowels.upper():
            indexes_vowels.append(i)

    char_list = list(s)
    while len(indexes_vowels) > 1:
        first_index = indexes_vowels[0]
        second_index = indexes_vowels[-1]
        indexes_vowels.pop(0)
        indexes_vowels.pop(-1)

        char_list[first_index], char_list[second_index] = char_list[second_index], char_list[first_index]

    return "".join(char_list)


print(solution("hello"))
