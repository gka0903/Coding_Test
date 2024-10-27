# 나이트 움직일 수 있는 방식으로 좌표 주어졌을 때 몇 군대나 갈 수 있나
# 8 X 8 체스판

location = input()
y = ord(location[0]) - ord('a') + 1
x = int(location[1])
result = 0

moving = [(-2, 1), (-2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2), (2, 1), (2, -1)]

for move in moving:
    dy = y + move[0]
    dx = x + move[1]

    if 8 < dy or dy < 1 or dx < 1 or dx > 8:
        continue

    result += 1

print(result)
