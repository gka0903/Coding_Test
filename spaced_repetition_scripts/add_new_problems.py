import os
from datetime import datetime

import pandas as pd

# --- 설정 (사용자 환경에 맞게 수정) ---

# 1. 문제 파일들이 저장된 폴더 경로를 지정하세요.
#    스크린샷에 표시된 경로 예시: '/Users/iseungho/Desktop/study/algorithm/programmers'
PROBLEMS_DIR = '/Users/hamhyeongbum/coding_test/문제'

# 2. 리뷰 스케줄 CSV 파일 이름을 지정하세요.
CSV_FILENAME = 'reviews_schedule.csv'


# ------------------------------------


def add_new_problems_to_schedule():
    """
    문제 폴더를 스캔하여 reviews_schedule.csv에 없는 새 문제를 추가합니다.
    """
    try:
        # 1. 기존 리뷰 스케줄(CSV)을 읽어옵니다.
        df = pd.read_csv(CSV_FILENAME)
        # 이미 등록된 문제들을 집합(set)으로 만들어 빠르게 조회할 수 있도록 합니다.
        existing_questions = set(df['question'].unique())
        print(f"✅ '{CSV_FILENAME}' 파일에서 {len(existing_questions)}개의 기존 문제를 불러왔습니다.")

    except FileNotFoundError:
        print(f"❌ 오류: '{CSV_FILENAME}' 파일을 찾을 수 없습니다.")
        print("💡 'init_schedule.py'를 먼저 실행하여 파일을 생성해주세요.")
        return

    try:
        # 2. 문제 폴더에 있는 모든 파일 목록을 가져옵니다.
        files_in_folder = os.listdir(PROBLEMS_DIR)
        # .py 확장자를 가진 파이썬 파일만 대상으로 필터링합니다.
        problem_files = {f for f in files_in_folder if f.endswith('.py')}
        print(f"📂 '{PROBLEMS_DIR}' 폴더에서 {len(problem_files)}개의 문제 파일을 찾았습니다.")

    except FileNotFoundError:
        print(f"❌ 오류: 문제 폴더 '{PROBLEMS_DIR}'를 찾을 수 없습니다.")
        print("💡 코드의 'PROBLEMS_DIR' 변수 경로를 올바르게 수정해주세요.")
        return

    # 3. CSV에 아직 없는 새로운 문제 파일들을 찾아냅니다.
    new_problems = list(problem_files - existing_questions)

    # 4. 새로운 문제가 없으면 메시지를 출력하고 종료합니다.
    if not new_problems:
        print("\n✨ 새로운 문제가 없습니다. 모든 문제가 이미 스케줄에 등록되어 있습니다.")
        return

    # 5. 새로운 문제가 있으면 CSV에 추가합니다.
    print(f"\n🆕 {len(new_problems)}개의 새로운 문제를 발견했습니다:")
    for problem in new_problems:
        print(f"  - {problem}")

    # 오늘 날짜를 YYYY-MM-DD 형식의 문자열로 준비합니다.
    today_str = datetime.today().strftime('%Y-%m-%d')

    # 추가할 데이터들을 리스트 형태로 만듭니다.
    new_data = [{'question': problem, 'created_date': today_str} for problem in new_problems]

    # 새로운 데이터를 DataFrame으로 변환합니다.
    new_df = pd.DataFrame(new_data)

    # 기존 DataFrame에 새로운 DataFrame을 합칩니다.
    updated_df = pd.concat([df, new_df], ignore_index=True)

    # 업데이트된 DataFrame을 다시 CSV 파일로 저장합니다.
    updated_df.to_csv(CSV_FILENAME, index=False)

    print(f"\n✅ '{CSV_FILENAME}' 파일에 새로운 문제들을 성공적으로 추가했습니다.")


if __name__ == '__main__':
    add_new_problems_to_schedule()
