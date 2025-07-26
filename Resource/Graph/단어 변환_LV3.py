from collections import deque


def check_different(w1, w2):
    count = 0

    for i in range(len(w1)):
        if w1[i] == w2[i]:
            count += 1

    return len(w1) - count


def groupSetByRule(words):
    group = {}

    for i in range(len(words)):
        word = words[i]

        for w in words:
            if word == w:
                continue

            if check_different(word, w) == 1:
                group.setdefault(word, set()).add(w)

    return group


def solution(begin, target, words):
    queue = deque()
    group = groupSetByRule(words)
    checked = set()

    for word in words:
        if check_different(word, begin) == 1:
            queue.append((word, 1))
            checked.add(word)

    while queue:
        word, depth = queue.popleft()

        if word == target:
            return depth

        for w in group[word]:
            if w not in checked:
                queue.append((w, depth + 1))
                checked.add(w)

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
