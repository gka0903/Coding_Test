# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            l = []
            for i in range(qLen):
                n = q.popleft()
                if n:
                    l.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if l:
                r.append(l)
        return r
