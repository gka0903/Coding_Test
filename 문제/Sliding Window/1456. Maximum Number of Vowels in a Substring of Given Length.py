def solution(s, k):
    maximum_number = 0
    current_number = 0
    vowel = 'aeiou'

    for i in range(len(s)):
        if s[i] in vowel:
            current_number += 1
        if i >= k and s[i - k] in vowel:
            current_number -= 1

        if current_number > maximum_number:
            maximum_number = current_number
        #
        # if maximum_number == k

    return maximum_number


print(solution("abciiidef", 3))
