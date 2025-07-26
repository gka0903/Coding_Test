import os
import pandas as pd
from datetime import datetime, timedelta

# 복습 주기 (일 단위)
intervals = [1, 4, 7, 14, 21]
filename = 'reviews_schedule.csv'

def init_schedule():
    if os.path.exists(filename):
        print(f"⚠️ '{filename}' already exists. Delete or back it up if you want to reinitialize.")
        return
    # 빈 데이터프레임 생성
    df = pd.DataFrame(columns=[
        'question',         # 복습할 문제 또는 키워드
        'created_date',     # 등록 날짜 (YYYY-MM-DD)
        'interval_index',   # 현재 주기 인덱스 (0부터)
        'next_review_date', # 다음 복습 예정일 (YYYY-MM-DD)
        'review_history'    # 복습 이력 (리스트 형식)
    ])
    df.to_csv(filename, index=False)
    print(f"✅ '{filename}' has been created with headers. Please add your items manually.")

if __name__ == '__main__':
    init_schedule()
