def solution(n) :
    sum = 0
    for i in n:
        i = int(i)
        if sum + i > sum * i:
            sum = sum + i
        else:
            sum = sum * i
      
    return sum


print(solution('02984'))
print(solution('567'))