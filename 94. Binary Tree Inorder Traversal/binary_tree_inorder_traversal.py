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
    def inorder(self, root, ans):
        if(root is None):
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.inorder(root, ans)
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        inorder = []
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
        return inorder
