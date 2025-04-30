def solution(s):
    s_list = s.split()
    first_string = ""
    second_string = ""

    while s_list:
        if s_list:
            first_string = s_list[0] if first_string == "" else s_list[0] + " " + first_string
            s_list.pop(0)

        if s_list:
            second_string += s_list[-1] if second_string == "" else " " + s_list[-1]
            s_list.pop(-1)

    if second_string == "":
        return first_string
    
    return second_string + " " + first_string


print(solution("a good   example"))
