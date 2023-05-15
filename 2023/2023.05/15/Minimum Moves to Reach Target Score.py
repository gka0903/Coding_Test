def solution(target, maxDoubles):
    count = 0
    while target != 1:
        if target % 2 == 0 and maxDoubles > 0:
            target //= 2
            maxDoubles -= 1
            count += 1
        elif target % 2 != 0 and maxDoubles == 0:
            count += target
            return count - 1
        else:
            target -= 1
            count += 1
    return count


print(solution(19, 2))
