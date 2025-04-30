def solution(n):
    n_count = bin(n).count('01')

    for i in range(n + 1, 1000000):
        check_count = bin(i).count('01')
        if check_count == n_count:
            return i


print(solution(78))
print(solution(15))
