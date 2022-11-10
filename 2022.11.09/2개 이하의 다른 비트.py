def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            num = i + 1
            answer.append(num)
        else:
            bin_number = "0" + format(i, 'b')
            bin_index = bin_number.rfind("0")
            number_list = list(bin_number)
            number_list[bin_index] = '1'
            number_list[bin_index + 1] = '0'
            result_list = "".join(number_list)
            result = int(result_list, 2)
            answer.append(result)

    return answer


print(solution([2, 7]))
