import os
from datetime import datetime, timedelta

import pandas as pd

# --- 설정 (사용자 환경에 맞게 수정) ---
PROBLEMS_DIR = '/Users/hamhyeongbum/coding_test/문제'
CSV_FILENAME = 'reviews_schedule.csv'
INTERVALS = [1, 4, 7, 14, 21]
# --- ✨ 핵심 수정: 컬럼명 변경 ---
FINAL_COLUMNS = ['question', 'created_date', 'interval_value', 'next_review_date', 'review_today']


def get_files_in_folder():
    """문제 폴더에서 .py 파일 목록을 가져옵니다."""
    try:
        return {f for f in os.listdir(PROBLEMS_DIR) if f.endswith('.py')}
    except FileNotFoundError:
        print(f"❌ 오류: 문제 폴더 '{PROBLEMS_DIR}'를 찾을 수 없습니다.")
        return None


def add_new_problems(df, files_in_folder):
    """DataFrame에 없는 새로운 문제를 추가합니다."""
    print("--- 1. 새로운 문제 파일 확인 시작 ---")
    existing_questions = set(df['question'].unique()) if not df.empty else set()
    new_problems = list(files_in_folder - existing_questions)

    if not new_problems:
        print("✨ 새로운 문제가 없습니다.\n")
        return df

    print(f"🆕 {len(new_problems)}개의 새로운 문제를 발견하여 추가합니다:")
    today_str = datetime.today().strftime('%Y-%m-%d')

    new_data = [{'question': problem, 'created_date': today_str} for problem in new_problems]

    new_df = pd.DataFrame(new_data)
    updated_df = pd.concat([df, new_df], ignore_index=True)
    print("✅ 새로운 문제들을 스케줄에 추가했습니다.\n")
    return updated_df


def recalculate_all_schedules(df):
    """
    모든 항목의 스케줄을 '생성일'과 '오늘'을 기준으로 완전히 재계산합니다.
    """
    print("--- 2. 전체 복습 일정 재계산 시작 ---")
    if df.empty:
        print("✨ 스케줄이 비어있어 재계산할 항목이 없습니다.\n")
        return df

    today = datetime.today().date()

    for i, row in df.iterrows():
        created_date = datetime.strptime(row['created_date'], '%Y-%m-%d').date()
        days_passed = (today - created_date).days

        # --- ✨ 핵심 수정: interval_index 대신 interval_value 계산 ---
        correct_index = -1
        for idx, interval_days in enumerate(INTERVALS):
            if days_passed >= interval_days:
                correct_index = idx

        # 인덱스에 해당하는 실제 간격 값으로 저장 (없으면 0)
        interval_value = INTERVALS[correct_index] if correct_index != -1 else 0
        df.at[i, 'interval_value'] = int(interval_value)
        # -----------------------------------------------------------

        # 오늘 복습 여부 결정
        if days_passed in INTERVALS:
            df.at[i, 'review_today'] = 'O (복습 필요)'
        else:
            df.at[i, 'review_today'] = 'X (대기)'

        # 다음 복습 날짜 계산
        next_interval_index = correct_index + 1
        if next_interval_index < len(INTERVALS):
            days_to_add = INTERVALS[next_interval_index]
            next_date = (created_date + timedelta(days=days_to_add)).strftime('%Y-%m-%d')
            df.at[i, 'next_review_date'] = next_date
        else:
            df.at[i, 'next_review_date'] = 'Completed'

    print("✅ 모든 항목의 스케줄을 성공적으로 재계산했습니다.\n")
    return df


def main():
    """메인 실행 함수"""
    try:
        df = pd.read_csv(CSV_FILENAME) if os.path.exists(CSV_FILENAME) else pd.DataFrame(
            columns=['question', 'created_date'])
    except Exception as e:
        print(f"❌ CSV 파일을 읽는 중 오류가 발생했습니다: {e}")
        return

    files_in_folder = get_files_in_folder()
    if files_in_folder is None:
        return

    # 폴더에 없는 파일 정보는 스케줄에서 제거
    if not df.empty:
        df = df[df['question'].isin(files_in_folder)].reset_index(drop=True)

    # 새로운 문제 추가 (생성일만 기록)
    df = add_new_problems(df, files_in_folder)

    # 모든 스케줄 정보를 '오늘' 날짜 기준으로 새로고침
    df = recalculate_all_schedules(df)

    # 최종적으로 필요한 열만 선택하여 CSV 파일에 저장
    for col in FINAL_COLUMNS:
        if col not in df.columns:
            df[col] = None
    df_to_save = df[FINAL_COLUMNS]
    df_to_save['interval_value'] = df_to_save['interval_value'].astype(int)

    df_to_save.to_csv(CSV_FILENAME, index=False)
    print(f"🎉 모든 작업이 완료되었습니다. '{CSV_FILENAME}' 파일이 업데이트되었습니다.")


if __name__ == '__main__':
    main()
