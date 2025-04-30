def solution(n):
    answer = ""
    n = list(str(n))
    n.sort(reverse = True)
    #fuction join
    print("".join(n))
    for i in n:
        answer += i
    
    answer = int(answer)
    
    return answer


print(solution(118372))