def make_review_row(start):
    """
    start: 'YYYY-MM-DD' 형식 문자열 또는 datetime.date 객체
    반환값: "| YYYY-MM-DD | YYYY-MM-DD | ... | YYYY-MM-DD |" 형태의 문자열
    """
    # 입력을 date 객체로 변환
    if isinstance(start, str):
        start = datetime.strptime(start, "%Y-%m-%d").date()
    # 리뷰 간격 리스트
    intervals = [0, 1, 3, 7, 14, 30]
    # 각 날짜 계산해서 문자열로 포맷
    dates = [(start + timedelta(days=d)).strftime("%Y-%m-%d") for d in intervals]
    # 파이프(|)로 연결된 마크다운 행 생성
    return "| " + " | ".join(dates) + " |"


# 문제 입력 및 리뷰 스케줄 추가
from datetime import datetime, timedelta
# 필요한 모듈 import

problems = []

# 사용자로부터 문제명과 틀린 날짜를 입력받습니다.
problem_name = input("문제명을 입력하세요: ").strip()
wrong_date = input("틀린 날짜를 입력하세요 (YYYY-MM-DD): ").strip()

# 문자열을 date 객체로 변환
start_date = datetime.strptime(wrong_date, "%Y-%m-%d").date()

# 복습 간격과 레이블 정의
intervals = [0, 1, 3, 7, 14, 30]
labels = ["틀린 날짜", "1차 복습", "2차 복습", "3차 복습", "4차 복습", "5차 복습"]

# 문제 항목 생성
entry = {"문제명": problem_name}
for label, days in zip(labels, intervals):
    entry[label] = (start_date + timedelta(days=days)).strftime("%Y-%m-%d")

# 리스트에 추가
problems.append(entry)

# 결과 출력
print("현재 problems 리스트:")
for p in problems:
    print(p)

# problems.py 파일에 새로운 문제 항목을 추가합니다.
import json

# 새로운 항목을 dict 형태의 문자열로 포맷합니다.
entry_str = json.dumps(entry, ensure_ascii=False, indent=4)
# problems.py 파일을 읽어서 리스트의 닫는 대괄호 위치를 찾습니다.
with open("problems.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 닫는 대괄호 직전에 새 항목을 추가할 수 있도록 파일을 재작성합니다.
with open("problems.py", "w", encoding="utf-8") as f:
    for line in lines:
        if line.rstrip().endswith("]") and not line.strip().startswith("#"):
            # 리스트 마지막에 쉼표를 확인하고 추가
            f.write("    " + entry_str.replace("\n", "\n    ") + ",\n")
        f.write(line)
print("problems.py에 새 항목이 추가되었습니다.")
