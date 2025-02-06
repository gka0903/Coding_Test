def solution(strs):
    hash_table = {}
    for i in range(len(strs)):
        sorted_str = "".join(sorted(strs[i]))
        if sorted_str in hash_table:
            hash_table[sorted_str].append(strs[i])
        else:
            hash_table[sorted_str] = [strs[i]]

    answer = list(hash_table.values())

    return answer


# Example usage
print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
