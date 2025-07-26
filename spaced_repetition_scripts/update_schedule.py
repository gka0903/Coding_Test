from datetime import datetime, timedelta

import pandas as pd

# 복습 주기 (일 단위)
intervals = [1, 4, 7, 14, 21]
filename = 'reviews_schedule.csv'


def update_schedule():
    # CSV 읽기
    df = pd.read_csv(filename, parse_dates=['next_review_date', 'created_date'])
    today = pd.Timestamp(datetime.today().date())

    # --- Initialize missing columns and fields ---
    # next_review_date: if missing column, create; if NaT, set to created_date + first interval
    if 'next_review_date' not in df.columns:
        df['next_review_date'] = df['created_date'] + pd.to_timedelta(intervals[0], unit='d')
    else:
        df['next_review_date'] = pd.to_datetime(df['next_review_date'])
        mask_date = df['next_review_date'].isna()
        df.loc[mask_date, 'next_review_date'] = df.loc[mask_date, 'created_date'] + pd.to_timedelta(intervals[0],
                                                                                                    unit='d')

    # interval_index: if missing column, create with 0; else fill NaN and ensure integer
    if 'interval_index' not in df.columns:
        df['interval_index'] = 0
    else:
        df['interval_index'] = df['interval_index'].fillna(0).astype(int)

    # review_history: if missing column, create empty list string; else fill NaN
    if 'review_history' not in df.columns:
        df['review_history'] = '[]'
    else:
        df['review_history'] = df['review_history'].fillna('[]')
    # -----------------------------------------------

    # 오늘 복습할 항목
    mask = df['next_review_date'] <= today
    # 오늘 복습할 항목 출력
    if mask.any():
        print("오늘 복습할 항목:")
        # print(df.loc[mask])
        print("\t" + "\n\t".join(df.loc[mask, 'question']))
    if not mask.any():
        print("ℹ️ No items scheduled for review today.")
        return

    for idx in df[mask].index:
        # 복습 이력 업데이트
        history = df.at[idx, 'review_history']
        # review_history 칼럼이 문자열이라면 eval 후 리스트 처리
        if isinstance(history, str):
            history = eval(history)
        history.append(today.strftime('%Y-%m-%d'))
        df.at[idx, 'review_history'] = history

        # 다음 주기 인덱스 업데이트
        current_i = int(df.at[idx, 'interval_index'])
        next_i = min(current_i + 1, len(intervals) - 1)
        df.at[idx, 'interval_index'] = next_i

        # 다음 복습 날짜 업데이트
        df.at[idx, 'next_review_date'] = today + timedelta(days=intervals[next_i])

    # Calculate days until next review for all items
    df['days_until_review'] = (df['next_review_date'] - today).dt.days
    # Reorder columns: ensure days_until_review comes before interval_index
    cols = list(df.columns)
    # Move 'days_until_review' to position before 'interval_index'
    if 'days_until_review' in cols and 'interval_index' in cols:
        cols.insert(cols.index('interval_index'), cols.pop(cols.index('days_until_review')))
        df = df[cols]
    # CSV 저장
    df.to_csv(filename, index=False)
    print(f"✅ Updated review schedule for {mask.sum()} items.")


if __name__ == '__main__':
    update_schedule()
