def solution(book_time):
    times = [0] * 2000
    for i, j in book_time:
        a = list(map(int, i.split(':')))
        b = list(map(int, j.split(':')))
        first_time = (a[0] * 60 + a[1])
        second_time = (b[0] * 60 + b[1] + 9)
        for index in range(first_time, second_time + 1):
            times[index] += 1
    return max(times)


print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
