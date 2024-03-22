def solution(s, goal):
    comp_s = s + s
    goal_len = len(goal)

    if goal_len < len(s):
        return False

    for i in range(0, len(comp_s) - goal_len):
        if goal == comp_s[i:i + goal_len]:
            return True

    return False


print(solution("abcde", "cdeab"))
