import sys

input = sys.stdin.readline
trees = {}
total_count = 0
cnt = 0

while True:
    tree = input().rstrip()

    if not tree:
        break

    total_count += 1

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

    cnt += 1

sorted_tree = sorted(trees.items(), key=lambda x: (x[0]))

for tree, count in sorted_tree:
    num = (count / cnt) * 100
    print(tree, f"{num:.4f}")
