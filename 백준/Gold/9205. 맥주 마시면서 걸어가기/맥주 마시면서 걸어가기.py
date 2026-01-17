import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def beer():
    N = int(input())
    sy, sx = map(int, input().split())
    visited = [False] * N
    stores = []

    for _ in range(N):
        cy, cx = map(int, input().split())
        stores.append((cy, cx))

    ty, tx = map(int, input().split())

    def dfs(y, x):
        if abs(ty - y) + abs(tx - x) <= 1000:
            return True

        for i in range(N):
            if abs(stores[i][0] - y) + abs(stores[i][1] - x) <= 1000:
                if not visited[i]:
                    visited[i] = True

                    if dfs(stores[i][0], stores[i][1]):
                        return True

        return False

    if dfs(sy, sx):
        print("happy")
    else:
        print("sad")


T = int(input())
for _ in range(T):
    beer()
