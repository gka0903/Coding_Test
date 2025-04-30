def solution(info, n, m):
    min_a_trace = float('inf')
    visited = set()

    def dfs(index, a_sum, b_sum):
        print(f"DFS 호출 -> index: {index}, a_sum: {a_sum}, b_sum: {b_sum}")
        nonlocal min_a_trace

        if a_sum >= n or b_sum >= m:
            print(" → 경찰에 잡힘. 종료.")
            return

        if len(info) == index:
            print(f" → 모든 물건 처리 완료. a_sum: {a_sum}, 최소값 갱신 시도.")
            min_a_trace = min(min_a_trace, a_sum)
            return

        state = (index, a_sum, b_sum)
        if state in visited:
            return
        visited.add(state)

        # A가 훔침
        print(f"A가 {index}번 물건 훔침 → +{info[index][0]} 흔적")
        dfs(index + 1, a_sum + info[index][0], b_sum)

        # B가 훔침
        print(f"B가 {index}번 물건 훔침 → +{info[index][1]} 흔적")
        dfs(index + 1, a_sum, b_sum + info[index][1])

    dfs(0, 0, 0)
    return min_a_trace if min_a_trace != float('inf') else -1


# [[1, 2], [2, 3], [2, 1]]	4	4	2
# [[1, 2], [2, 3], [2, 1]]	1	7	0
# [[3, 3], [3, 3]]	7	1	6
# [[3, 3], [3, 3]]	6	1	-1

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
