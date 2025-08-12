import os
from datetime import datetime, timedelta

import pandas as pd

# --- 설정 (사용자 환경에 맞게 수정) ---

# 1. 문제 파일들이 저장된 폴더 경로
PROBLEMS_DIR = '/Users/hamhyeongbum/coding_test/문제'

# 2. 리뷰 스케줄 CSV 파일 이름
CSV_FILENAME = 'reviews_schedule.csv'

# 3. 복습 간격 (일 단위) - 마지막 복습을 마치면 목록에서 제거됨
INTERVALS = [1, 4, 7, 14, 21]

# ------------------------------------

# CSV 파일에 유지할 최종 열 목록
FINAL_COLUMNS = ['question', 'created_date', 'interval_index', 'next_review_date']


def add_new_problems(df):
    """
    문제 폴더를 스캔하여 CSV에 없는 새 문제를 찾아 DataFrame에 추가합니다.
    """
    print("--- 1. 새로운 문제 파일 확인 시작 ---")
    try:
        files_in_folder = {f for f in os.listdir(PROBLEMS_DIR) if f.endswith('.py')}
    except FileNotFoundError:
        print(f"❌ 오류: 문제 폴더 '{PROBLEMS_DIR}'를 찾을 수 없습니다.")
        return df

    existing_questions = set(df['question'].unique()) if not df.empty else set()
    new_problems = list(files_in_folder - existing_questions)

    if not new_problems:
        print("✨ 새로운 문제가 없습니다.\n")
        return df

    print(f"🆕 {len(new_problems)}개의 새로운 문제를 발견했습니다:")
    today_str = datetime.today().strftime('%Y-%m-%d')
    new_data = []
    for problem in new_problems:
        print(f"  - {problem}")
        new_data.append({
            'question': problem,
            'created_date': today_str,
            'interval_index': 0,
            'next_review_date': (datetime.today() + timedelta(days=INTERVALS[0])).strftime('%Y-%m-%d'),
        })

    if not new_data:
        return df

    new_df = pd.DataFrame(new_data)
    updated_df = pd.concat([df, new_df], ignore_index=True)
    print("✅ 새로운 문제들을 스케줄에 추가했습니다.\n")
    return updated_df


def update_review_schedule(df):
    """
    복습 날짜가 지난 항목들의 다음 복습 일정을 업데이트합니다.
    """
    print("--- 2. 복습 일정 업데이트 시작 ---")
    today = datetime.today().date()
    updated_count = 0

    for i, row in df.iterrows():
        if pd.isna(row['next_review_date']) or row['next_review_date'] == 'Completed':
            continue

        next_review_date = datetime.strptime(row['next_review_date'], '%Y-%m-%d').date()

        if next_review_date <= today:
            updated_count += 1
            print(f"🔄 복습 항목 업데이트: {row['question']}")

            # 다음 복습 간격 설정
            current_interval_index = int(row['interval_index']) + 1
            df.at[i, 'interval_index'] = current_interval_index

            if current_interval_index < len(INTERVALS):
                days_to_add = INTERVALS[current_interval_index]
                new_next_review_date = (datetime.today() + timedelta(days=days_to_add)).strftime('%Y-%m-%d')
                df.at[i, 'next_review_date'] = new_next_review_date
            else:
                # 마지막 복습 완료 표시 (이후 단계에서 삭제됨)
                df.at[i, 'next_review_date'] = 'Completed'

    if updated_count == 0:
        print("✨ 오늘 복습할 항목이 없습니다.\n")
    else:
        print(f"✅ 총 {updated_count}개의 항목을 업데이트했습니다.\n")
    return df


def remove_completed_reviews(df):
    """
    모든 복습 주기를 마친 항목을 DataFrame에서 제거합니다.
    """
    print("--- 3. 완료된 복습 항목 제거 시작 ---")
    completed_index = len(INTERVALS)
    initial_rows = len(df)

    # 완료된 항목들 필터링
    completed_items = df[df['interval_index'] >= completed_index]

    if not completed_items.empty:
        print("🗑️ 다음 항목들의 복습이 완료되어 목록에서 제거합니다:")
        for _, row in completed_items.iterrows():
            print(f"  - {row['question']}")

    # 완료되지 않은 항목들만 남기고, 최종 열만 선택
    df_cleaned = df[df['interval_index'] < completed_index]

    removed_count = initial_rows - len(df_cleaned)
    if removed_count > 0:
        print(f"✅ 총 {removed_count}개의 완료된 항목을 제거했습니다.\n")
    else:
        print("✨ 완료되어 제거할 항목이 없습니다.\n")
    return df_cleaned


def main():
    """
    메인 실행 함수
    """
    try:
        if not os.path.exists(CSV_FILENAME):
            print(f"'{CSV_FILENAME}' 파일이 없어 새로 생성합니다.")
            df = pd.DataFrame(columns=FINAL_COLUMNS)
        else:
            df = pd.read_csv(CSV_FILENAME)
    except Exception as e:
        print(f"❌ CSV 파일을 읽는 중 오류가 발생했습니다: {e}")
        return

    # DataFrame이 비어있지 않다면, 타입 일관성 유지
    if not df.empty:
        df['interval_index'] = pd.to_numeric(df['interval_index'], errors='coerce').fillna(0).astype(int)

    # 1. 새로운 문제 추가
    df = add_new_problems(df)

    # 2. 복습 일정 업데이트
    df = update_review_schedule(df)

    # 3. 완료된 항목 제거
    df = remove_completed_reviews(df)

    # 4. 최종적으로 필요한 열만 선택하여 CSV 파일에 저장
    df_to_save = df[FINAL_COLUMNS]
    df_to_save.to_csv(CSV_FILENAME, index=False)

    print(f"🎉 모든 작업이 완료되었습니다. '{CSV_FILENAME}' 파일이 업데이트되었습니다.")


if __name__ == '__main__':
    main()
