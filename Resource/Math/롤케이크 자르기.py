from collections import Counter


def solution(topping):
    answer = 0
    p1 = Counter([topping[0]])
    p2 = Counter(topping[1:])

    for i in range(1, len(topping)):
        t = topping[i]
        if t in p1:
            p1[t] += 1
        else:
            p1[t] = 1

        p2[t] -= 1
        if p2[t] == 0:
            del p2[t]

        if len(p1) == len(p2):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
