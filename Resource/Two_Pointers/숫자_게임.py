def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    a_pointer = 0
    b_pointer = 0

    while a_pointer < len(A) and b_pointer < len(B):
        if A[a_pointer] < B[b_pointer]:
            answer += 1
            a_pointer += 1
            b_pointer += 1
        else:
            b_pointer += 1

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
