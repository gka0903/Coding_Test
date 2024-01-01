from collections import Counter


def solution(k, tangerine):
    count = 0
    # collections.Counter(a) : a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환합니다.  {문자 : 개수} 형태
    # collections.Counter(a).most_common(n)   : a의 요소를 세어, 최빈값 n개를 반환합니다. (리스트에 담긴 튜플형태로)
    a = Counter(tangerine).most_common()
    print(a)
    for i in a:
        count += 1
        k -= i[1]
        if k <= 0:
            break
    return count




print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
