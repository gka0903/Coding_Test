def solution(N, K):
    count = 0
    while N != 1:
        if N % K == 0:
            N //= K
        else :
            N -= 1
        count += 1
        
        
    return count

print(solution(17, 4))
print(solution(25, 5))


