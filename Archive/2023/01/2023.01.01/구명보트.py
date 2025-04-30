def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[a] + people[b] <= limit:
            answer += 1
            a += 1
        b -= 1
    return len(people) - answer


print(solution([70, 50, 80, 50], 100))