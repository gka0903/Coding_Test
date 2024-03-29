# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def diameterOfBinaryTree(root) -> int:
    res = [0]

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)

        res[0] = max(res[0], left + right + 2)

        return max(left, right) + 1

    dfs(root)
    return res[0]
