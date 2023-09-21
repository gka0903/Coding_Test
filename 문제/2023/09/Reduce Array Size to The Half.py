def solution(arr):
    count = {}
    min_short = len(arr) // 2
    for i in arr:
        if i in count:
            count[i] += 1
            pass
        else:
            count[i] = 1
    sorted_count = list(sorted(count.items(), key=lambda item: item[1], reverse=True))

    for result in range(len(sorted_count)):
        min_short -= sorted_count[result][1]
        if min_short <= 0:
            return result + 1
    return -1


print(solution([5, 5, 3, 3, 3, 3, 5, 2, 2, 7]))
