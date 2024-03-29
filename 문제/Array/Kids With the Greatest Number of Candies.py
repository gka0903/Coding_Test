def solution(candies, extraCandies):
    result = [False] * len(candies)
    m_candy = 0
    for candy in candies:
        if m_candy < candy:
            m_candy = candy
    for index in range(len(candies)):
        if candies[index] + extraCandies >= m_candy:
            result[index] = True

    return result


print(solution([2, 3, 5, 1, 3], 3))
