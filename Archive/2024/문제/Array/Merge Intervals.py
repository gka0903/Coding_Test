def merge(intervals):
    intervals.sort()
    i = 1
    while i < len(intervals):
        for j in range(i):
            if intervals[j][1] >= intervals[i][0]:
                first = intervals[j][0] if intervals[j][0] < intervals[i][0] else intervals[i][0]
                second = intervals[j][1] if intervals[j][1] > intervals[i][1] else intervals[i][1]
                intervals[i] = [first, second]
                intervals.pop(j)
                i -= 1
                break
        i += 1
    return intervals


def solution(intervals):
    intervals.sort()
    result = []
    for i in range(len(intervals)):
        if not result:
            result.append(intervals[i])
        if intervals[i][0] <= result[-1][1]:
            second = result[-1][1] if result[-1][1] > intervals[i][1] else intervals[i][1]
            result[-1] = [result[-1][0], second]
        else:
            result.append(intervals[i])
    return result


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [0, 2], [3, 5]]))

print(solution([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution([[1, 4], [0, 2], [3, 5]]))
