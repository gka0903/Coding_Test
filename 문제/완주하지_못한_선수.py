# from collections import Counter
#
#
# def solution(participant, completion):
#     left = Counter(participant) - Counter(completion)
#
#     return left.popitem()[0]
#
# # hash 풀이
# def solution(participant, completion):
#     answer = ""
#     temp = 0
#     dic = {}
#
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#
#     for com in completion:
#         temp -= hash(com)
#
#     answer = dic[temp]
#
#     return answer

# 복습 4주기
def solution(participant, completion):
    hash_code = 0
    dic = {}

    for part in participant:
        code = hash(part)
        hash_code += code
        dic[code] = part

    for c in completion:
        hash_code -= hash(c)

    return dic[hash_code]


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
