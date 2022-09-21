import math
def solution(n, m):
    gcd = math.gcd(n, m)
    answer = [gcd, int((n * m) / gcd)]
        
    return answer

print(solution(3, 12))
print(solution(2, 5))