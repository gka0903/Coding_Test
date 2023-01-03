def solution(n, a, b):
    answer = 0
    arr = str(a) + str(b)
    a = []
    bracket = ''
    for i in range(1, n + 1):
        bracket += str(i)
    split_data = list(map(''.join, zip(*[iter(bracket)] * 2)))

    for j in split_data:
        bracket = ''
        if j == arr:
            return answer


    return answer


print(solution(8, 4, 7))
