def solution(n, left, right):
    answer = []
    start = (left // n, left % n)
    end = (right // n, right % n)

    for i in range(start[0], end[0] + 1):
        number = (i + 1)

        for j in range(n):
            if i < j:
                number += 1

            if i == start[0] and j < start[1]:
                continue

            answer.append(number)

            if i == end[0] and j == end[1]:
                break

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
