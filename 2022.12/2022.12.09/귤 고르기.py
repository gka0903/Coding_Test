from collections import Counter


def solution(k, tangerine):
    count = 0
    c = Counter(tangerine)
    a = c.most_common()
    for i in a:
        count += 1
        k -= i[1]
        if k <= 0:
            break
    return count




print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
