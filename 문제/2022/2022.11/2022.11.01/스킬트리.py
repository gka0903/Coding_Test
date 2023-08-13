def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_tree = ""
        for j in i:
            if j in skill:
                skill_tree += j

        # for _ in range(len(skill_tree)):
        #     if skill_tree[_] == skill[_]:
        #         result = True
        #     else:
        #         result = False
        #         break
        # if result:
        #     answer += 01

        if skill[:len(skill_tree)] == skill_tree:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
