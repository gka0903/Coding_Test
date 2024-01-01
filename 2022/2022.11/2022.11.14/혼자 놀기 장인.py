def solution(cards):
    answer = 0
    for x in cards:
        boxs = [0] * len(cards)
        first_num, target = 0, x
        while True:
            if boxs[target - 1] == 0:
                boxs[target - 1] = 1
                first_num += 1
                target = cards[target - 1]
            else:
                break

        second_boxs = []
        for i in range(len(cards)):
            if boxs[i] == 0:
                second_boxs.append(cards[i])

        second_num = 0
        for j in second_boxs:
            second_sub, target = 0, j
            while True:
                if boxs[target - 1] == 0:
                    boxs[target - 1] = 1
                    second_sub += 1
                    target = cards[target - 1]
                else:
                    second_num = max(second_sub, second_num)
                    break

        answer = max(answer, first_num * second_num)
    return answer



print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
