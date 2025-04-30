def solution(strings, n):
    strings.sort()
    arr = []
    answer = []
    print(strings)
    for i in strings:
        arr.append([i[n], i])
    arr.sort()
    print(arr)
    for i in arr:
        answer.append(i[1])
    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
