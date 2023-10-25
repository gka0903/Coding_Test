def solution(sequence, k):
    start, end = 0, 0
    current_sum = sequence[0]
    results = []
    while start < len(sequence) and end < len(sequence):
        if current_sum == k:
            results.append([start, end])
            current_sum -= sequence[start]
            start += 1
        elif current_sum < k:
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1
    if not results:
        return [0, 0]

    result = [0, 0]
    check = float('inf')
    for i in results:
        index_distance = i[1] - i[0]
        if index_distance < check:
            check = index_distance
            result = i
    return result


print(solution([2, 2, 2, 2, 2], 6))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
