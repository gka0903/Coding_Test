# dict을 만들어서
# 찾은 최소값들을 거기다가 저장

def solution(keymap, targets):
    answer = []
    min_press = {}

    for key in keymap:
        for i in range(len(key)):
            if key[i] in min_press and i + 1 > min_press[key[i]]:
                continue

            min_press[key[i]] = i + 1
    print(min_press)

    for target in targets:
        count = 0

        for t in target:
            if t not in min_press:
                count = -1
                break

            count += min_press[t]

        answer.append(count)

    return answer


# print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))
print(solution(["AA"], ["B"]))
