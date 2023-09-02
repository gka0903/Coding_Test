def longestCommonPrefix(strs):
    strs.sort(key=lambda x: len(x))

    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            print(strs[0][i], strs[j][i])
            if strs[0][i] != strs[j][i]:
                return strs[0][:i]

    return strs[0]


print(longestCommonPrefix(["flower", "flow", "flight"]))
