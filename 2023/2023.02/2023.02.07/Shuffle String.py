def restoreString(s, indices):
    answer = ''
    l = len(indices)
    for i in range(l):
        for j in range(l):
            if i == indices[j]:
                answer += s[j]
                break
    return answer


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
