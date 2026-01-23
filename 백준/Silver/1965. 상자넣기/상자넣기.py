import sys

input = sys.stdin.readline
N = int(input())
boxes = list(map(int, input().split()))
longest_subsequence = [boxes[0]]
result = 1


def binary_search(s, e, target):
    idx = e

    while s <= e:
        m = (s + e) // 2

        if longest_subsequence[m] >= target:
            idx = m
            e = m - 1
        else:
            s = m + 1

    return idx


for i in range(1, len(boxes)):
    if boxes[i] > longest_subsequence[-1]:
        longest_subsequence.append(boxes[i])
        result += 1
    else:
        box_idx = binary_search(0, result - 1, boxes[i])
        longest_subsequence[box_idx] = boxes[i]

print(result)
