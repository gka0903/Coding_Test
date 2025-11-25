stack = []
seq = []
index = 0

N = int(input())
for _ in range(N):
    s = int(input())
    seq.append(s)

num = 1

result = []

while num <= N:
    if stack and stack[-1] == seq[index]:
        result.append("-")
        stack.pop()
        index += 1
        continue
    else:
        result.append("+")
        stack.append(num)

    num += 1

while index <= N:
    if stack and stack[-1] == seq[index]:
        result.append("-")
        stack.pop()
        index += 1
        continue
    else:
        break

if stack:
    print("NO")
else:
    for i in result:
        print(i)
