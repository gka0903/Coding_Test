def solution(order):
    main_con = [i for i in range(1, len(order) + 1)]
    truck, sub_con = [], []
    target = 0

    for i in range(len(main_con)):
        if sub_con and sub_con[-1] == order[target]:
            truck.append(sub_con.pop(-1))
            target += 1

        sub_con.append(main_con[i])

        if sub_con and sub_con[-1] == order[target]:
            truck.append(sub_con.pop(-1))
            target += 1

    if sub_con:
        while sub_con and sub_con[-1] == order[target]:
            truck.append(sub_con.pop(-1))
            target += 1

    return len(truck)


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))

