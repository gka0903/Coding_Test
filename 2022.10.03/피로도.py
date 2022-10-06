from itertools import permutations

def solution(k, dungeons):
    dungeons_array = list(permutations(dungeons))
    dungeons_max = 0
    
    for i in dungeons_array:
        dungeons_sep = 0
        my_life = k
        for j in i:
            if my_life >= j[0]:
                my_life -= j[1]
                dungeons_sep += 1
            else :
                break
        dungeons_max = max(dungeons_max, dungeons_sep)
        
    
    return dungeons_max;

print(solution(80,[[80,20],[50,40],[30,10]]))
#permutation 함수로 순열 배열을 만듦
#순열로 나온 모든 경우의 수를 완전탐색
#max 함수로 가장 여러번 던전에 갈 수 있는 수를 저장

