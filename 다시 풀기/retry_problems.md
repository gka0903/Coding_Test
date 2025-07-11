### 🔁 도둑의 흔적 최소화

- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/389480?language=python3)
- 유형: DFS + 상태 메모이제이션
- 주요 개념: 완전 탐색, 가지치기, visited 처리
- 오답 이유: 상태 중복 관리 미흡, 흔적 최소화 조건 최적화 실패 가능성
- 다시 볼 포인트:
    - `dfs(index, a_sum, b_sum)` 구조 이해
    - `visited`를 `set()`과 3차원 배열로 비교
    - `min_a_trace`의 갱신 시점 및 조건 처리

### 🔁 땅따먹기

- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12913)
- 유형: DP (Top-down / Bottom-up)
- 주요 개념: 인접 행 선택 제한, 점수 누적 최적화
- 오답 이유: 이전 열의 상태 추적 부족, 중복 계산 발생 가능성
- 다시 볼 포인트:
    - `land[i][j] += max(land[i-1][k]) (단, k ≠ j)` 점화식 이해
    - Top-down 방식에서 메모이제이션 구조 비교 (lru_cache vs dict)
    - Bottom-up 방식의 점화식 구현과 테이블 갱신 흐름

### 🔁 정수 삼각형

- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43105)
- 유형: DP (Bottom-up / Top-down)
- 주요 개념: 삼각형 형태의 누적 최댓값 계산, 인접한 두 수 중 큰 값을 선택하여 누적
- 오답 이유: 경계 조건 처리 미흡, 중복 계산으로 인한 시간 초과
- 다시 볼 포인트:
    - `dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]` 점화식 이해
    - Top-down 방식에서 메모이제이션 구조 비교 (`lru_cache` vs `dict`)
    - Bottom-up 방식의 점화식 구현과 테이블 갱신 흐름