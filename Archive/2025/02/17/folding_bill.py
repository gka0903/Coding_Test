def solution(wallet, bill):
    answer = 0
    w_min = min(wallet)
    w_max = max(wallet)
    b_min = min(bill)
    b_max = max(bill)

    while w_min < b_min or w_max < b_max:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2

        b_min = min(bill)
        b_max = max(bill)

        answer += 1

    return answer


print(solution([50, 50], [100, 241]))
