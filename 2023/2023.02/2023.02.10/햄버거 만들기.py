# 01 : 빵
# 2 : 야채
# 3 : 고기
def solution(ingredient):
    check_arr = [1, 2, 3, 1]
    answer = 0
    arr = []
    for i in ingredient:
        arr.append(i)
        if len(arr) >= 4 and arr[len(arr) - 4::] == check_arr:
            del arr[len(arr) - 4::]
            answer += 1
    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
