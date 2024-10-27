def solution(want, number, discount):
    for i in range(10):
        if discount[i] in want:
            number[want.index(discount[i])] -= 1

    index = 0
    count = 0

    for i in range(10, len(discount)):

        if discount[index] in want:
            number[want.index(discount[index])] += 1
        index += 1

        if discount[i] in want:
            number[want.index(discount[i])] -= 1

        for num in number:
            if num > 0:
                break
            count += 1
            break

    return count


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
