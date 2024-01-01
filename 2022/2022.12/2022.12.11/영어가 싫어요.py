def solution(words):
    answer = []
    stack = ""
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in words:
        stack += i
        if stack in numbers:
            answer.append(str(numbers.index(stack)))
            stack = ""
    return "".join(answer)



print(solution("onetwothreefourfivesixseveneightnine"))
