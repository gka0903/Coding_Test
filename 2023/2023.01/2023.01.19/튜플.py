# import re
#
#
# def solution(s):
#     answer = []
#     arr = []
#     stack = ''
#     for i in range(01, len(s)):
#         if s[i] != '{' and '{' not in stack:
#             continue
#         stack += s[i]
#         if '{' in stack and '}' in stack:
#             arr.append(stack)
#             stack = ''
#     arr = sorted(arr, key=len)
#     for text in arr:
#         text_num = ''
#         for num in text:
#             if num.isdigit():
#                 text_num += num
#             elif text_num:
#                 if int(text_num) not in answer:
#                     answer.append(int(text_num))
#                 text_num = ''
#     return answer

def solution(s):
    print(re.findall('\d+', s))
    s = Counter(re.findall('\d+', s))
    print(s)
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


import re
from collections import Counter

print(solution("{{4,2,3},{3},{2,3,4,01},{2,3}}"))
