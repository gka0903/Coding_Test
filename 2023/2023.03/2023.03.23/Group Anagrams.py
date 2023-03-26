def groupAnagrams(strs):
    if len(strs) <= 1:
        return strs
    index_table = [0] * len(strs)
    arr = []
    for i in range(len(strs)):
        string = "".join(sorted(list(strs[i])))
        if string not in arr:
            arr.append(string)
            index_table[i] = arr.index(string)
        else:
            index_table[i] = arr.index(string)
    answer = [[] for _ in range(len(arr))]
    for index in range(len(strs)):
        answer[index_table[index]].append(strs[index])
    return answer


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
