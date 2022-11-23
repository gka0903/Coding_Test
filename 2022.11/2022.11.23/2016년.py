from datetime import datetime, date


def what_day_is_it(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()

    return days[day]


def solution(a, b):
    d = date(2016, a, b)
    return what_day_is_it(d)


print(solution(5, 24))
