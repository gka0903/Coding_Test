def main(num):
    n_len = len(num)
    mid = n_len // 2
    left_sum = sum([int(i) for i in num[:mid] if i != '?'])
    right_sum = sum([int(i) for i in num[mid:] if i != '?'])
    left_count = num[:mid].count('?')
    right_count = num[mid:].count('?')
    return aliceWin(left_sum, right_sum, left_count, right_count) or aliceWin(right_sum, left_sum, right_count,
                                                                              left_count)


def aliceWin(left_sum, right_sum, left_count, right_count):
    for i in range(right_count + left_count):
        print(left_sum, right_sum)
        if i % 2 == 0:
            if left_count > 0:
                left_sum += 9
                left_count -= 1
            else:
                right_count -= 1
        else:
            if right_count > 0:
                right_sum += 9
                right_count -= 1
            else:
                left_count -= 1
    return left_sum != right_sum


print(main("?3295???"))
