# Recursive
# T.C.->O(n)
# S.C.->O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, level, ans):
        if not node:
            return
        if len(ans) == level:
            ans.append([])  # Start a new level
        ans[level].append(node.val)
        self.traverse(node.left, level + 1, ans)
        self.traverse(node.right, level + 1, ans)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.traverse(root, 0, ans)
        return ans


# Iterative
# T.C.->O(n)
# S.C.->O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)

        return ans
