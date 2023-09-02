class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

apple = TreeNode(1)
apple.left = TreeNode(2)
apple.right = TreeNode(3)


def solution(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return solution(a.left, b.left) and solution(a.left, b.left)


print(solution(tree, apple))
