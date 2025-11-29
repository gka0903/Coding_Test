import re


# 첫 풀이
def parse(index, file_name):
    file_name = file_name.lower()

    parse_file_name = re.match(r"([a-z-.\s]+)(\d+)", file_name)
    head, number = parse_file_name.groups()

    return head, int(number), index


def solution(files):
    answer = []
    p_files = []

    # files를 parse로 해서 다른 리스트를 만들어
    # 리스트를 기준으로 정리
    # 리스트 기준대로 안에 인덱스 있으니까 그걸 리턴

    for index in range(len(files)):
        p_file = (parse(index, files[index]))
        p_files.append(p_file)

    p_files.sort(key=lambda x: (x[0], x[1], x[2]))

    for p in p_files:
        answer.append(files[p[-1]])

    return answer


# 두 번째
def solution2(files):
    answer = []
    re_files = []

    for index in range(len(files)):
        current_file = files[index]
        f = re.match(r"([^\d]+)(\d+)", current_file.lower())
        head, number = f.groups()
        re_files.append((head, int(number), index))

    re_files.sort(key=lambda x: (x[0], x[1], x[2]))

    return [files[i[-1]] for i in re_files]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
