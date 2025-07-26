from collections import Counter


def solution(want, number, discount):
    window = discount[:10]
    window_dict = Counter(window)
    want_dict = {w: n for w, n in zip(want, number)}
    answer = 0

    if window_dict == want_dict:
        answer += 1

    for i in range(10, len(discount)):
        product = discount[i]
        pre_product = discount[i - 10]

        if product in window_dict:
            window_dict[product] += 1
        else:
            window_dict[product] = 1

        window_dict[pre_product] -= 1

        if window_dict[pre_product] == 0:
            del window_dict[pre_product]

        if window_dict == want_dict:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
