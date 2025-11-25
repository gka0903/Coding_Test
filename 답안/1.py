def solution(ability):
    # 최종 결과(최대 능력치 합)를 저장할 변수
    answer = 0
    # 학생 수와 종목 수 계산
    num_students = len(ability)
    num_events = len(ability[0])

    # 각 학생이 이미 대표로 뽑혔는지 확인하기 위한 리스트
    # 예: visited[0]이 True이면 0번 학생은 이미 다른 종목 대표임
    visited = [False] * num_students

    # 깊이 우선 탐색(DFS) 함수 (백트래킹)
    # event_idx: 현재 대표를 뽑고 있는 종목의 인덱스
    # current_sum: 현재까지 구성된 팀의 능력치 합계
    def dfs(event_idx, current_sum):
        # nonlocal: solution 함수의 answer 변수를 직접 수정하겠다는 의미
        nonlocal answer

        # [종료 조건] 모든 종목의 대표를 다 뽑았다면
        if event_idx == num_events:
            # 현재 팀의 점수(current_sum)가 기록된 최고점(answer)보다 높으면 갱신
            answer = max(answer, current_sum)
            return

        # 모든 학생을 순회하며 현재 종목(event_idx)의 대표를 뽑는 모든 경우를 탐색
        for student_idx in range(num_students):
            # 만약 해당 학생이 아직 어떤 종목의 대표도 아니라면
            if not visited[student_idx]:
                # 1. 현재 학생을 대표로 뽑음 (체크)
                visited[student_idx] = True

                # 2. 다음 종목의 대표를 뽑기 위해 재귀 호출
                #    (현재 학생의 능력치를 합계에 더해서 넘겨줌)
                dfs(event_idx + 1, current_sum + ability[student_idx][event_idx])

                # 3. ★가장 중요★ 다른 조합을 탐색하기 위해, 위에서 뽑았던 학생을 다시 안 뽑은 상태로 되돌림 (체크 해제)
                visited[student_idx] = False

    # 0번 종목부터 탐색 시작 (초기 점수 합계는 0)
    dfs(0, 0)

    return answer


# --- 테스트를 위한 예제 코드 ---
# 예제 1
ability1 = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
result1 = solution(ability1)
print(f"예제 1 결과: {result1}")  # 예상 결과: 210

# 예제 2
ability2 = [[20, 30], [30, 20], [20, 30]]
result2 = solution(ability2)
print(f"예제 2 결과: {result2}")  # 예상 결과: 60
