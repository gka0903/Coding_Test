def solution(spells, potions, success):
    # potions 정렬
    # spells 반복
    # spells[i] * potions[i] > success 인 인덱스 찾기
    # 그 인덱스 기준 -1 하면서 불가능한 인덱스 찾기
    # 인덱스 기준 potions 길이 체크 해서 pairs 갱신

    potions.sort()
    pairs = []

    for i in range(len(spells)):

        left = 0
        right = len(potions) - 1
        index = len(potions)

        while left <= right:

            mid = (left + right) // 2
            product = spells[i] * potions[mid]
            if product >= success:
                right = mid - 1
                index = mid
            else:
                left = mid + 1

        pairs.append(len(potions) - index)

    return pairs


# print(solution([5, 1, 3], [1, 2, 3, 4, 5], 7))
# print(solution([15, 8, 19], [38, 36, 23], 328))
print(solution([9, 39], [35, 40, 22, 37, 29, 22], 320))
