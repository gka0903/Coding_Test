def solution(s):
    zero_count = 0
    sep_count = 0
    while s != '1':
        sum_text = ""
        for i in s:
                if i == "0":
                    zero_count += 1
                    pass
                else:
                    sum_text += i
        s = format(bin(int(len(sum_text)))[2:])
        sep_count += 1 
        print(s, zero_count, sep_count)
    

    return [sep_count, zero_count]

print(solution("110010101001"))