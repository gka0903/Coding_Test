def solution(routes):
    answer = 1

    # 정렬
    routes.sort(key=lambda x: x[1])
    cam_point = routes[0][1]

    # 진입 기준 확인 반복
    for i in range(1, len(routes)):
        if routes[i][0] <= cam_point:
            continue

        answer += 1
        cam_point = routes[i][1]

    return answer


#  [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
