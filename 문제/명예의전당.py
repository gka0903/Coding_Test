def binary(fame, score):
    first, end = 0, len(fame)

    while first < end:
        mid = (first + end) // 2
        if fame[mid] <= score:
            first = mid + 1
        else:
            end = mid

    return fame[:first] + [score] + fame[first:]


def solution(k, score):
    fame = []
    answer = []

    for s in score:
        fame = binary(fame, s)  # 이진 탐색으로 점수 삽입
        if len(fame) > k:
            fame.pop(0)  # 명예의 전당 크기가 k를 초과하면 최솟값 제거
        answer.append(fame[0])  # 최하위 점수 추가

    return answer
