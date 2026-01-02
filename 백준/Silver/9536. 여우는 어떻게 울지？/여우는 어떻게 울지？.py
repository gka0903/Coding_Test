import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    all_animals_say = list(input().split())
    not_fox = set()
    s = ""

    while True:
        s = input().strip()

        if s == "what does the fox say?":
            break

        animal, goes, say = s.split()
        not_fox.add(say)

    for i in range(len(all_animals_say)):
        if all_animals_say[i] not in not_fox:
            print(all_animals_say[i], end=" ")
