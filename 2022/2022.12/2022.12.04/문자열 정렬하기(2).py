def solution(my_string):
    arr = list(my_string.lower())
    arr.sort()
    return "".join(arr)



print(solution("Bcad"))