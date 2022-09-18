def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == False :
            absolutes[i] = -absolutes[i]
    
    for i in absolutes:
        answer += i
            
    return answer

print(solution([4,7,12], [True, False, True]))