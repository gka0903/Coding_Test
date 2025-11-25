import sys

input = sys.stdin.readline
stack = []


# push X: 정수 X를 스택에 넣는 연산이다.
def push(x):
    stack.append(int(x))


# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())


# size: 스택에 들어있는 정수의 개수를 출력한다.
def size():
    print(len(stack))


# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if not stack:
        print(1)
    else:
        print(0)


# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    if not stack:  # 스택이 비어있으면
        print(-1)
    else:
        print(stack[-1])


N = int(input())
for i in range(N):
    command = input().split()

    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()
