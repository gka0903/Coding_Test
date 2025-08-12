def solution(record):
    dic = {}
    answer = []

    for r in record:
        command = r.split(" ")
        c = command[0]
        uid = command[1]
        nick = command[2] if len(command) == 3 else ""

        if c == "Enter":
            dic[uid] = nick

        # if c == "Leave":
        #     message = dic[uid] + "님이 나갔습니다."

        if c == "Change":
            dic[uid] = nick

    for r in record:
        command = r.split(" ")
        c = command[0]
        uid = command[1]
        message = ""

        if c == "Enter":
            message = dic[uid] + "님이 들어왔습니다."

        if c == "Leave":
            message = dic[uid] + "님이 나갔습니다."

        if message != "":
            answer.append(message)

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
