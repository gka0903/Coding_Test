import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(input().strip())

alpha = ['a', 'n', 't', 'i', 'c']
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']


def choose_alpha(n, start):
    global result
    if n == 0:
        result = max(result, check())
        return
    for i in range(start, len(alpha_list)):
        alpha.append(alpha_list[i])
        choose_alpha(n - 1, i + 1)
        alpha.pop()


def check():
    result = 0
    for words in arr:
        isRead = True
        for i in range(4, len(words) - 4):
            if words[i] not in alpha:
                isRead = False
                break
        if isRead:
            result += 1
    return result


result = 0
if K < 5:
    print(result)
else:
    choose_alpha(K - 5, 0)
    print(result)

# 백트랙킹
# anta로 시작하고 tica로 끝나니까 최소로 필요한 단어수는 5개(a,c,i,n,t)
# 01. alpha에 위 5개 알파벳을 추가하고 K가 5보다 작으면 0출력
# 2. K가 5이상이면
#   - 알파벳 고르기 (choose_alpha) : 백트랙킹으로 n개만큼 알파벳을 alpha리스트에 추가
#   - 읽을 수 있는 단어 개수 구하기 (check) : anta와 tica를 제외한 가운데 부분이 alpha에 있는지 체크
#   - 최댓값으로 result 초기화
# 3. result 출력 (걸린 시간)
