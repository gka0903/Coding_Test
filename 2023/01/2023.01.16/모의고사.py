def solution(answers):
    answer = []
    first_student = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    second_student = [2, 1, 2, 3, 2, 4, 2, 5]
    third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [[0, 1], [0, 2], [0, 3]]
    first_len, second_len, third_len = len(first_student), len(second_student), len(third_student)
    for i in range(len(answers)):
        check = answers[i]
        if check == first_student[i % first_len]:
            score[0][0] += 1
        if check == second_student[i % second_len]:
            score[1][0] += 1
        if check == third_student[i % third_len]:
            score[2][0] += 1
    max_score = max(score)[0]

    for i in score:
        if i[0] == max_score:
            answer.append(i[1])

    return answer


print(solution([1, 2, 3, 4, 5]))
