def solution(salary):
    min_salary = 1000000
    max_salary = 1000
    sum_salary = 0
    for i in salary:
        sum_salary += i
        if i < min_salary:
            min_salary = i
        if i > max_salary:
            max_salary = i
    avg = (sum_salary - max_salary - min_salary) / (len(salary) - 2)

    return avg


print(solution([8000, 9000, 2000, 3000, 6000, 1000]))
