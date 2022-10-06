def solution(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else :
            n -= 1
            count += 1
        
    return count

print(solution(5))
print(solution(6))
print(solution(16))
print(solution(5000))
#최대한 많이 나누는게 좋음


