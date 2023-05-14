def wordBreak(s, wordDict):
    return '다시'


print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

# https://leetcode.com/problems/word-break/submissions/931145957/
# s_len = len(s)
# dp = [False] * (s_len + 01)
# dp[0] = True
# for i in range(01, s_len + 01):
#     for j in range(i):
#         if dp[j] and s[j:i] in wordDict:
#             print(j, i, s[j:i])
#             dp[i] = True
#             break
# return dp[s_len]
