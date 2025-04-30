def solution(want, number, discount):
    for i in range(len(discount)):
        number_check = number
        print(number, number_check)
        for j in range(i, len(discount)):
            if discount[j] in want:
                number_check[want.index(discount[j])] -= 1
                if number_check[want.index(discount[j])] < 0:

                    break

        for _ in number_check:
            if _ == 0:
                result = True
            else:
                result = False
                break

        if result:
            return i

    return 0


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
