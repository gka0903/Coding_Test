import math


def solution(fees, records):
    answer = []
    # dict 두 가지(입출력 확인용, 계산용)
    entry_exit = {}
    calculater = {}

    # 출입 기록 정리
    for i in range(len(records)):
        time, car_number, history = records[i].split(" ")
        h, m = time.split(":")
        m = int(m) + int(h) * 60

        if car_number not in entry_exit:
            entry_exit[car_number] = m
        else:
            if car_number not in calculater:
                calculater[car_number] = m - entry_exit[car_number]
            else:
                calculater[car_number] += m - entry_exit[car_number]

            del entry_exit[car_number]

    # entry_exit에 값이 있다면 입차 하고 출차 x
    if entry_exit:
        for car_num in entry_exit:
            if car_num not in calculater:
                calculater[car_num] = (59 + (23 * 60)) - entry_exit[car_num]
            else:
                calculater[car_num] += (59 + (23 * 60)) - entry_exit[car_num]

    # 정리 후 계산
    # 작은 순으로 answer에 넣기
    for cal in sorted(calculater.items()):
        duration_time = cal[1]
        base_time, base_fee, unit_time, unit_fee = fees

        if duration_time <= base_time:
            answer.append(base_fee)
            continue

        fee = math.ceil((duration_time - base_time) / unit_time) * unit_fee
        answer.append(fee + base_fee)

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
