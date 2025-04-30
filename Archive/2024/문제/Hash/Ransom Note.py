def solution(ransomNote, magazine):
    hash_table = {}

    for i in magazine:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    for i in ransomNote:
        if i in hash_table:
            hash_table[i] -= 1
        else:
            return False

        if hash_table[i] < 0:
            return False

    return True


print(solution("aa", "aab"))
