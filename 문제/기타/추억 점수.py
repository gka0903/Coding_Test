def solution(name, yearning, photo):
    answer = []
    dic = {}
    for index in range(len(name)):
        dic[name[index]] = yearning[index]

    for p in photo:
        result = 0
        for person in p:
            if person in dic:
                result += dic[person]
        answer.append(result)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
