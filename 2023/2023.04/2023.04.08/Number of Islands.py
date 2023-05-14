def numIslands(grid):
    def dfs(x, y):
        if x <= -1 or x >= len(grid) or y <= -1 or y >= len(grid[0]):
            return False
        if int(grid[x][y]) == 1:
            grid[x][y] = 0
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j):
                count += 1

    return count


print(numIslands([
    ["01", "01", "01", "01", "0"],
    ["01", "01", "0", "01", "0"],
    ["01", "01", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
# https://leetcode.com/problems/number-of-islands/description/
