from datetime import datetime

from problems import problems


def get_due_problems(date_str: str):
    """
    주어진 날짜(date_str)에 해당하는 복습 일정이 있는 문제명을 리스트로 반환.
    date_str: 'YYYY-MM-DD' 형식 문자열
    """
    due = []
    for item in problems:
        # 각 키 중 날짜가 일치하는 단계가 있는지 체크
        for key, d in item.items():
            if key.endswith("복습") or key == "틀린 날짜":
                if d == date_str:
                    due.append(item["문제명"])
                    break
    return due


if __name__ == "__main__":
    today = input("오늘 날짜를 입력하세요 (YYYY-MM-DD): ").strip()
    try:
        # 입력 검증
        datetime.strptime(today, "%Y-%m-%d")
    except ValueError:
        print("날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형태로 입력해 주세요.")
        exit(1)

    due_list = get_due_problems(today)
    if due_list:
        print(f"{today}에 다시 풀어야 할 문제:")
        for name in due_list:
            print(f"- {name}")
    else:
        print(f"{today}에 다시 풀어야 할 문제는 없습니다.")
