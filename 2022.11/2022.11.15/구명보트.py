def solution(people, limit):
    check_people = [0] * len(people)
    people.sort()
    answer = 0

    for i in range(len(people)):
        check_boat = False
        if check_people[i] == 1:
            continue
        else:
            check_people[i] = 1
            for j in range(len(people) - 1, i, -1):
                if check_people[j] == 0 and people[i] + people[j] <= limit:
                    answer += 1
                    check_people[j] = 1
                    check_boat = True
                    break
            if not check_boat:
                answer += 1

    return answer


def solutions(people, limit):
    boat = 0
    people.sort(reverse=True)
    while people:
        if len(people) >= 2:
            if people[0] + people[-1] <= limit:
                boat += 1
                people.pop(0)
                people.pop(-1)
            else:
                people.pop(0)
                boat += 1
        else:
            people.pop()
            boat += 1

    return boat


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

print(solutions([70, 50, 80, 50], 100))
print(solutions([70, 80, 50], 100))
