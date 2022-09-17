def solution(n):
    answer = []
    answer = list(str(n))
    answer.reverse()
    answer = list(map(int, answer))
    
    return answer

print(solution(12345))