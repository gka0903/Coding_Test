def solution(sequence, k):
    start, end = 0, 0

    if k in sequence:
        index = sequence.index(k)
        return [index, index]

    while end < len(sequence) - 1:
        s = sum(sequence[start:end + 1])
        if s == k:
            return [start, end]
        elif s < k:
            end += 1
        else:
            start += 1


print(solution([2, 2, 2, 2, 2], 6))
