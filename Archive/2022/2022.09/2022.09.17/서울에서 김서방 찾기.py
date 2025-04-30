def solution(seoul):
    answer = ''
    sep = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 " + str(i) + "에 있다"

        sep += 1
        
    return answer

print(solution(["Jane", "Kim"]))

#function index, function format
def solution2(seoul):
        
    return "김서방은 {}에 있다".format(seoul.index("Kim"))

print(solution(["Jane", "June", "Billy","Kim", "Edie"]))