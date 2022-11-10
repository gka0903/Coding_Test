def solution(s):
    answer = False
    num_p = 0
    num_y = 0   
    
    for i in s:
        if i == "p" or i == "P":
            num_p += 1
        elif i == "y" or i == "Y":
            num_y += 1
            
    if num_p == num_y:
        answer = True

    return answer

print(solution("pyy"))
print(solution("pypypypypypypypyyyypypyypyppypypypypppyypypypypypyp"))
print(solution("ppyy"))