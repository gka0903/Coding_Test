def solution(n, words):
    stack = []
    count = 0
    answer = False
    for i in words:
        count += 1
        if i in stack:
            answer = True
            break
        if stack and stack[-1][-1] != i[0]:
            answer = True
            print(count)
            break

        stack.append(i)

    if not answer:
        return [0, 0]

    if count % n == 0:
        return[n, count // n]
    else:
        return[count % n, count // n + 1]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
