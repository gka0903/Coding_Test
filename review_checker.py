import subprocess
from datetime import datetime

# ==========================================
# ⚙️ 설정: 원하는 복습 주기를 입력하세요 (일 단위)
# 예: [1, 3, 7, 14, 30] -> 1일 전, 3일 전... 내용을 복습
REVIEW_CYCLES = [1, 3, 7, 14, 30, 60]
# ==========================================


def get_git_logs():
    """
    Git 커밋 로그를 가져옵니다.
    형식: YYYY-MM-DD|커밋메시지
    """
    try:
        # git log 명령어를 실행하여 날짜와 메시지만 가져옴
        # %ad: author date (short format YYYY-MM-DD), %s: subject
        max_cycle = max(REVIEW_CYCLES)
        cmd = [
            "git",
            "log",
            f"--since={max_cycle}.days.ago",
            "--pretty=format:%ad|%s",
            "--date=short",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

        if result.returncode != 0:
            print("❌ Git 저장소가 아니거나 로그를 불러올 수 없습니다.")
            return []

        return result.stdout.strip().split("\n")
    except FileNotFoundError:
        print("❌ Git이 설치되어 있지 않습니다.")
        return []


def check_review_topics():
    logs = get_git_logs()
    today = datetime.now().date()

    review_list = {}

    print(f"\n📅 **{today} 오늘의 복습 목록** 📅\n" + "=" * 40)

    for line in logs:
        if not line:
            continue

        try:
            date_str, message = line.split("|", 1)
            commit_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            # 경과일 계산 (오늘 - 커밋날짜)
            days_passed = (today - commit_date).days

            # 경과일이 복습 주기에 포함되는지 확인
            if days_passed in REVIEW_CYCLES:
                if days_passed not in review_list:
                    review_list[days_passed] = []
                review_list[days_passed].append(message)

        except ValueError:
            continue

    # 결과 출력
    if not review_list:
        print("🎉 오늘은 복습할 내용이 없습니다! 새로운 공부를 시작해보세요.")
    else:
        # 주기 순서대로 정렬하여 출력
        for days in sorted(review_list.keys()):
            print(f"\n🔔 {days}일 전 공부한 내용 (복습 주기: {days}일차)")
            for msg in review_list[days]:
                print(f"  - {msg}")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    check_review_topics()
