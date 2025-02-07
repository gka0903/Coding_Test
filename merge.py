import os
import sys


def main():
    # 1. 인자 체크
    if len(sys.argv) < 2:
        print("Usage: python merge.py <folder_name>")
        sys.exit(1)

    folder_path = sys.argv[1]

    # 2. 폴더 유효성 검사
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)

    # 3. 해당 폴더 안의 .py 파일만 추출
    py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

    if not py_files:
        print(f"No .py files found in directory: {folder_path}")
        sys.exit(0)

    # 4. 정렬 (원하는 순서가 있다면 자유롭게 조정 가능)
    py_files.sort()

    # 5. 병합할 마크다운 파일 이름 (폴더명 기반)
    merged_filename = f"merged_{os.path.basename(folder_path)}.md"

    # 6. 마크다운 파일로 병합하기
    with open(merged_filename, "w", encoding="utf-8") as outfile:
        for py_file in py_files:
            file_path = os.path.join(folder_path, py_file)

            # (선택) 각 파일마다 파일명을 헤더로 작성
            outfile.write(f"# {py_file}\n\n")

            # 파이썬 코드 블록 시작
            outfile.write("```python\n")

            # 실제 코드 읽어서 쓰기
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())

            # 파이썬 코드 블록 닫기
            outfile.write("\n```\n\n")

    print(f"✅ Merged {len(py_files)} Python files into '{merged_filename}'")


if __name__ == "__main__":
    main()
