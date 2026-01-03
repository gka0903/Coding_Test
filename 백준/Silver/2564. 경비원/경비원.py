import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

width, height = map(int, input().split())
N = int(input())
result = 0

# idx 0 dir
# idx 1 pos
stores = []

for _ in range(N):
    t_dir, t_pos = map(int, input().split())
    stores.append((t_dir, t_pos))

cur_dir, cur_pos = map(int, input().split())


def next_step(cur_dir, cur_pos, is_clockwise):
    if is_clockwise:
        if cur_dir == 1:
            return 4, 0, width - cur_pos
        if cur_dir == 2:
            return 3, height, cur_pos
        if cur_dir == 3:
            return 1, 0, cur_pos
        if cur_dir == 4:
            return 2, width, height - cur_pos
    else:
        if cur_dir == 1:
            return 3, 0, cur_pos
        if cur_dir == 2:
            return 4, height, width - cur_pos
        if cur_dir == 3:
            return 2, 0, height - cur_pos
        if cur_dir == 4:
            return 1, width, cur_pos


def move(cur_dir, cur_pos, target_dir, target_pos, is_clockwise, total):
    if cur_dir == target_dir:
        return abs(cur_pos - target_pos) + total

    next_dir, next_pos, add_distance = next_step(cur_dir, cur_pos, is_clockwise)

    return move(
        next_dir, next_pos, target_dir, target_pos, is_clockwise, total + add_distance
    )


for target_dir, target_pos in stores:
    clockwise_true = move(cur_dir, cur_pos, target_dir, target_pos, True, 0)
    clockwise_false = move(cur_dir, cur_pos, target_dir, target_pos, False, 0)

    result += min(clockwise_true, clockwise_false)


print(result)
