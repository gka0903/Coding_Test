n, m = map(int, input().split())
array = []
for i in range(n):
    row = list(map(int, input().strip()))  # 각 줄을 개별 숫자로 변환하여 리스트에 추가
    array.append(row)


def dfs(array, y, x
        ):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if array[y][x] == 1:
        return
    array[y][x] = 1
    dfs(array, x + 1, y)
    dfs(array, x - 1, y)
    dfs(array, x, y + 1)
    dfs(array, x, y - 1)


count = 0
for y in range(n):
    for x in range(m):
        if array[y][x] == 0:
            print(y, x)
            print(array)
            count += 1
            dfs(array, y, x)
            print(array)

print(count)
