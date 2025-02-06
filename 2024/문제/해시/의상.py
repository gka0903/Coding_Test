# dictionary 이용 같은 이름 거 숫자 올리기
# 그리고 계산
def solution(clothes):
    dic = {}
    for _, cloth in clothes:
        if cloth not in dic:
            dic[cloth] = 1
            continue

        dic[cloth] += 1

    result = 1
    for i in dic.values():
        result *= i + 1

    return result - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

# # gpt 개선안
# def solution2(clothes):
#     # 의상 종류별로 개수를 저장하는 딕셔너리 생성
#     dic = defaultdict(int)
#     for _, kind in clothes:
#         dic[kind] += 1
#
#     # 각 종류별로 (착용하지 않는 경우 포함)를 곱한 후 1을 뺌
#     result = 1
#     for count in dic.values():
#         result *= (count + 1)
#
#     return result - 1
