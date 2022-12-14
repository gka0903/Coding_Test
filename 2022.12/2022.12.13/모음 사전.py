from itertools import product


def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(6):
        for j in product(alphabet, repeat=i):
            arr.append("".join(j))
    arr.sort()
    return arr.index(word)


print(solution("AAAAE"))
