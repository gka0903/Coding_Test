def solution(num):
    answer = 0
    sep = 0
    while num != 1:
        if sep >= 500:
            return -1

        if num % 2 == 0:
            num //= 2
        else :
            num = num * 3 + 1
        
        sep += 1
    
    answer = sep
        
    return answer

print(solution(6))
print(solution(16))
print(solution(626331))